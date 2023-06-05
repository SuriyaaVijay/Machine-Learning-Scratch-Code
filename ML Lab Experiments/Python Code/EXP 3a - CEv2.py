import pandas as pd
import numpy as np

data = pd.read_csv ( "ce_dataset.csv" )
print ( "\n Data read from dataset.csv :\n\n" , data )

arr = np.array ( data )
print ( "\n Numpy array = " , arr )
X = arr [ : , : -1 ]
y = arr [ : , -1 ]
print ( "\n\n" , X , "\n\n" , y )

el = 0
while el < len ( y ) :
    if y [ el ] == "yes" :
        print ( "\n 1st Positive Sample ..\n Initializing Specific & General Hypotheses .." )
        break
    el += 1
    
specific = X [ el ]
general = [ [ '?' for x in range ( len ( X [ 0 ] ) ) ] for y in range ( len ( X [ 0 ] ) ) ]

def getHypotheses ( specific , general , ind ) :
    while ind < len ( y ) :
        if y [ ind ] == "yes" :
            print ( "\n Positive Sample .." )
            for hyp in range ( len ( specific ) ) :
                if specific [ hyp ] != X [ ind ] [ hyp ] :
                    specific [ hyp ] = '?'
                    general [ hyp ] [ hyp ] = '?'
        else :
            print ( "\n Negative Sample .." )
            for hyp in range ( len ( specific ) ) :
                general [ hyp ] [ hyp ] = specific [ hyp ] if specific [ hyp ] != X [ ind ] [ hyp ] else '?'
        ind += 1
    if len ( general ) > 1 :
        lst = [ '?' for x in range ( len ( specific ) ) ]
        while lst in general :
            general.remove ( lst )
    return specific , general

specific_hypothesis , general_hypothesis = getHypotheses ( specific , general , el + 1 )
print ( "\n General Hypotheses : " , general_hypothesis )
print ( "\n Specific Hypotheses : " , specific_hypothesis )