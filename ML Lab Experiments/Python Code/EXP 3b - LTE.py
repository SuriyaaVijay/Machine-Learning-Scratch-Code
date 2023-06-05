import pandas as pd
import numpy as np
import itertools

data = pd.read_csv ( "dataset.csv" )
print ( "\n Data read from dataset.csv :\n\n" , data )

arr = np.array ( data )
print ( "\n Numpy array = " , arr )
X = arr [ : , : -1 ]
y = arr [ : , -1 ]
print ( "\n\n" , X , "\n\n" , y )

iters = [ arr [ : , x ] for x in range ( len ( X [ 0 ] ) ) ]
print ( "\nb Iters = " , iters )

attr_labels = [ list ( set ( itr ) ) for itr in iters ]

for el in range ( len ( attr_labels ) ) :
    attr_labels [ el ].append ( '?' )
print ( "\n" , attr_labels )
combs = list ( itertools.product ( *attr_labels ) )
print ( "\n Initial set of Semantically Distinct Hypotheses : \n" )

def checkConsistency ( combs , el ) :
    acc = [ 1 for i in range ( len ( X [ 0 ] ) ) ]
    for ind in range ( len ( X ) ) :
        samp = X [ ind ]
        for x in range ( len ( samp ) ) :
            if y [ ind ] == "Yes" : 
                if combs [ el ] [ x ] == '?' or combs [ el ] [ x ] == samp [ x ] :
                    continue
                else :
                    acc [ x ] = 0
            else :
                if combs [ el ] [ x ] != samp [ x ] :
                    continue
    if 0 in acc :
        combs.pop ( el )
    print ( len ( combs ) )
    return combs , len ( combs )

el , lng = 0 , len ( combs )
while el < lng :
    combs , lng = checkConsistency ( combs , el )
    el += 1
    for cm in combs :
        print ( cm )