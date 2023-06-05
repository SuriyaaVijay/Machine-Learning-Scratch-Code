import numpy as np
import pandas as pd
import itertools as it

def get_combinations ( arr ) :
    subsets , filter , all_combs = [] , [] , []
    for i in range ( 1 , len ( arr ) + 1 ) :
        x = it.combinations ( arr , i )
        for comb in it.combinations ( arr , i ) :
            subsets.append ( list ( comb ) )
    for i in range ( 1 , len ( subsets ) ) :
        for comb in it.combinations ( subsets , i ) :
            unique = set ()
            for subset in comb :
                for element in subset :
                    if element in unique :
                        break
                    unique.add ( element )
                else :
                    continue
            else :
                all_combs.append ( list ( comb ) )
    for comb in all_combs :
        all_elements = []
        for subset in comb :
            all_elements.extend ( subset )
        if set ( all_elements ) == set ( arr ) :
            if ( len ( comb ) > 2 and len ( comb ) < len ( arr ) ) or ( len ( comb ) <= 2 ) :
                filter.append ( comb )
    return filter

def calc_total_gini ( arr ) :
    targets = arr [ : , -1 ]
    total_gini , tot = 1 , len ( targets )
    for el in list ( set ( targets ) ) :
        total_gini -= ( np.count_nonzero ( targets == el ) / tot ) ** 2
    return total_gini

def calc_sub_gini ( data , target_name , attribute , array ) :
    mask = data [ attribute ].isin ( array )
    sub_array  = data [ mask ]
    total_rows , gini = len ( sub_array ) , 1
    distinct_values = sub_array [ target_name ].unique()
    for value in distinct_values :
        num_rows = len ( sub_array [ sub_array [ target_name ] == value ] )
        gini -= ( num_rows / total_rows ) ** 2
    return total_rows , gini

def calc_gini ( data , target_name , attribute ) :
    attr_vals = data [ attribute ].unique ()
    all_subsets = get_combinations ( attr_vals )
    tot_rows , min_gini , best_subset = len ( np.array ( data ) ) , 1 , all_subsets [ 0 ]
    for subset in all_subsets :
        gini_subset = 0
        for el in subset :
            tup = calc_sub_gini ( data , target_name , attribute , el )
            gini_subset += ( tup [ 0 ] / tot_rows ) * tup [ 1 ]
        if gini_subset < min_gini :
            min_gini , best_subset = gini_subset , subset
    print ( best_subset , min_gini , "\n" )
    return best_subset , min_gini

def calc_Iteration ( data , attributes , target_name , target_vals ) :
    print ( "\n ITERATION\n" )
    arr , split_subset = np.array ( data ) , []
    total_gini , gini_max , attr_max = calc_total_gini ( arr ) , 0 , ""
    for attribute in attributes :
        print ( attribute )
        subset, min_gini = calc_gini ( data , target_name , attribute )
        curr_gini = round ( total_gini - min_gini , 4 )
        if curr_gini > gini_max :
            gini_max , attr_max , split_subset = curr_gini , attribute , subset
    return attr_max , gini_max , split_subset

def build_cart_tree ( data , attributes , target_name , target_vals ) :
    if len ( set ( data [ 'Job Offer' ] ) ) == 1 :
        return { 'Job Offer' : data [ 'Job Offer' ].iloc [ 0 ] }
    best_splitting_attribute, min_gini , best_splitting_subset = calc_Iteration ( data , attributes , target_name , target_vals )
    tree = { best_splitting_attribute: {} }
    for subset in best_splitting_subset :
        subset_data = data [ data [ best_splitting_attribute ].isin ( subset ) ].drop ( [ best_splitting_attribute ], axis=1 )
        attributes = subset_data.columns [ : len ( subset_data.columns ) - 1 : ]        
        subtree = build_cart_tree ( subset_data , attributes , target_name , target_vals )
        tree [ best_splitting_attribute ] [ tuple ( subset ) if len ( subset ) > 1 else subset [ 0 ] ] = subtree        
    return tree

def print_tree ( node , indent = 0 ) :
    for key , value in node.items () :
        print ( ' ' * indent + str ( key ) )
        if isinstance ( value , dict ) :
            print_tree ( value , indent + 5 )
        else :
            print ( ' ' * ( indent + 5 ) + str ( value ) )

data = pd.read_csv ( 'data7CART.csv' )
print (data )
attributes , target_name = [ 'CGPA' , 'Interactiveness' , 'Practical Knowledge' , 'Communication Skill' ] , 'Job Offer'
target_vals = data [ target_name ].unique ()
tree = build_cart_tree ( data , attributes , target_name , target_vals )
print ( "\n Final TREE\n ----------\n" )
print_tree ( tree )