import pandas as pd
import numpy as np

data = pd.read_csv ( "dataset.csv" )
print ( "\n Data read from dataset.csv :\n\n" , data )

arr = np.array ( data )
attributes = arr [ : , : -1 ]
print ( "\n Storing attributes in numpy array :\n\n" , attributes )

target = [ x [ -1 ] for x in arr ]
print ( "\n Target = " , target )

for ind , val in enumerate ( target ) :
    if val == "Yes" :
        specific_hypothesis = attributes [ ind ].copy ()
        break

for ind , val in enumerate ( attributes ) :
    if target [ ind ] == "Yes" :
        for el in range ( len ( specific_hypothesis ) ) :
            if val [ el ] != specific_hypothesis [ el ] :
                specific_hypothesis [ el ] = '?'

print ( "\n Final Hypothesis = " , specific_hypothesis )