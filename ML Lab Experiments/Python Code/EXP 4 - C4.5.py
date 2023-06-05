import pandas as pd
import numpy as np
 
def calc_total_entropy(data,target_name,target_val):
    size = data.shape[0]
    total_entropy=0
    
    for i in target_val:
        count = data[data[target_name] == i].shape[0]
        entropy = -(count/size)*np.log2(count/size)
        total_entropy += entropy
    
    return total_entropy
 
def calc_entropy(data,target_name,target_val):
    size = data.shape[0]
    total_entropy=0
    
    for i in target_val:
        count = data[data[target_name] == i].shape[0]
        entropy = 0
        if count !=0:    
            entropy = -(count/size)*np.log2(count/size)
        total_entropy += entropy
 
    return total_entropy

def calc_split_info(split):
    split_info = 0
    for el in split :
        split_info += -(el*np.log2(el))
    return split_info
 
def calc_gain(attribute,data,target_name,target_val):
    list_ = data[attribute].unique()
    size = data.shape[0]
    gain = 0.0
    probs = []
    
    for i in list_:
        t_data = data[data[attribute] == i]
        count = data[data[attribute] == i].shape[0]
        entropy = calc_entropy(t_data, target_name, target_val)
        prob = count/size
        probs.append ( prob )
        gain += prob*entropy
 
    split = calc_split_info(probs)
    return calc_total_entropy(data, target_name, target_val) - gain, split 
    
def ratio_attribute(data,target_name,target_val):
    list_ = data.columns.drop(target_name)
    max_ratio = -1
    info_feat = None
    matrix = []
    for i in list_:
        gain, split = calc_gain(i,data,target_name,target_val)
        matrix.append([i, "Gain = " + str(gain), "Split = " + str(split)])
        ratio = gain / split
        if max_ratio < ratio:
            max_ratio = ratio
            info_feat = i
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ( "\n".join(table) , "\n" )
    return info_feat
 
def generate_tree(attribute,data,target_name,target_val):
    count_dict=data[attribute].value_counts(sort = False)
    tree = {}
    
    for value,count in count_dict.iteritems():
        feat_data = data[data[attribute] == value]
        pure = False
        for t in target_val:
            class_count = feat_data[feat_data[target_name] == t].shape[0]
            if class_count == count:
                tree[value] = t 
                data = data[data[attribute] != value]
                pure = True
        if not pure:
            tree[value] = '?'
        
    return tree,data
    
def make_tree(root,prev,data,target_name,target_val):
    if data.shape[0] != 0:
        max_info_attribute = ratio_attribute(data, target_name, target_val)
        tree,data = generate_tree(max_info_attribute, data, target_name, target_val)
        next_root = None
        
        if prev != None:
            root[prev] = dict()
            root[prev][max_info_attribute] = tree
            next_root = root[prev][max_info_attribute]
 
        else:
            root[max_info_attribute] = tree
            next_root = root[max_info_attribute]
            
        for node,branch in list(next_root.items()):
            if branch == "?":
                 feat_data = data[data[max_info_attribute] == node]
                 make_tree(next_root,node,feat_data,target_name,target_val)
                
def c4_5(data,target_name):
    tree = {}
    target = data[target_name].unique()
    make_tree(tree,None,data,target_name,target)
    return tree
    
data = pd.read_csv('data6C45.csv')
tree = c4_5(data,'Job Offer')
print ( tree )