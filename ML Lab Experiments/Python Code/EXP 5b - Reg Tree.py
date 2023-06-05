import pandas as pd
import numpy as np
import math

def calc_total_avg_sd ( arr ) :
    targets = arr [ : , -1 ]
    sd , avg = 0 , np.mean ( targets )
    for el in targets :
        sd += ( el - avg ) ** 2
    sd = math.sqrt ( sd / len ( targets ) )
    return avg , sd

def calc_attr_avg_sd ( data , attribute , total_sd ) :
    attr_vals , arr = data [ attribute ].unique () , np.array ( data )
    sd_instance , weighted_sd = [] , 0
    for val in attr_vals :
        sub_data = data [ data [ attribute ] == val ]
        sub_target_vals = np.array ( sub_data ) [ : , -1 ]
        sub_sd , sub_avg , lng = 0 , np.mean ( sub_target_vals ) , len ( sub_target_vals ) 
        for el in sub_target_vals :
            sub_sd += ( el - sub_avg ) ** 2
        sub_sd = math.sqrt ( sub_sd / lng )
        sd_instance.append ( [ lng , sub_sd ] )
    for x in sd_instance :
        weighted_sd += round ( ( x [ 0 ] / len ( arr ) ) * x [ 1 ] , 4 )
    sd_reduction = total_sd - weighted_sd
    return sd_reduction , attr_vals

def calc_Iteration ( data , attributes ) :
    arr , max_sd_reduction = np.array ( data ) , 0
    tot_avg , tot_sd = calc_total_avg_sd ( arr )
    attribute_vals , best_attribute = [] , None
    for attribute in attributes :
        attr_sd_reduction , attr_vals = calc_attr_avg_sd ( data , attribute , tot_sd )
        if attr_sd_reduction > max_sd_reduction :
            max_sd_reduction , best_attribute = attr_sd_reduction , attribute
            attribute_vals = attr_vals
    return best_attribute , attribute_vals

def build_reg_tree ( data , attributes , target_name , target_vals ) :
    best_attribute , split_values = calc_Iteration ( data , attributes )
    if best_attribute is None :
        return data [ target_name ].mean ()
    node = {}
    for value in split_values :
        sub_data = data [ data [ best_attribute ] == value ]
        sub_data = sub_data.drop ( [ best_attribute ] , axis=1 )
        attributes = sub_data.columns.drop ( target_name )
        if sub_data.empty :
            node [ value ] = data [ target_name ].mean ()
        else :
            subtree = build_reg_tree ( sub_data , attributes , target_name , target_vals )
            node [ value ] = subtree
    return { best_attribute : node }

def print_tree ( node , indent = 0 ) :
    for key , value in node.items () :
        print ( ' ' * indent + str ( key ) )
        if isinstance ( value , dict ) :
            print_tree ( value , indent + 4 )
        else :
            print ( ' ' * ( indent + 4 ) + str ( value ) )

data = pd.read_csv ( 'data8RegTree.csv' )
attributes , target_name = [ 'Assessment' , 'Assignment' , 'Project' ] , 'Result'
target_vals = data [ target_name ].unique ()
tree = build_reg_tree ( data , attributes , target_name , target_vals )
print ( "\n Final TREE\n --------------\n" )
print_tree ( tree )