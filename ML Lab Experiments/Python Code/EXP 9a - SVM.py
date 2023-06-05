import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv ( "svm_dataset.csv" )
print ( "\n Data read from dataset.csv :\n\n" , data )

arr = np.array ( data )
X = arr [ : , : -1 ]
y = arr [ : , -1 ]
print ( "\n X :\n" , X , "\n\n y :\n" , y )

w = np.zeros ( len ( X [ 0 ] ) )
b , lr , epochs = 0 , 0.1 , 500

for epoch in range ( epochs ) :
    for i , x in enumerate ( X ) :
        if y [ i ] * ( np.dot ( X [ i ] , w ) - b ) >= 1 :
            w -= lr * ( 2 * 1 / epochs * w )
        else :
            w -= lr * (2 * 1 / epochs * w - np.dot ( X [ i ] , y [ i ] ) )
            b -= lr * y [ i ]

print ( "\n Weight vector : " , w )
print ( "Bias term : " , b )

plt.scatter ( X [ : , 0 ] , X [ : , 1 ] , c = y )
x_min, x_max = X [ : , 0 ].min () - 1 , X [ : , 0 ].max () + 1
y_min, y_max = X [ : , 1 ].min () - 1 , X [ : , 1 ].max () + 1
xx , yy = np.meshgrid ( np.arange ( x_min , x_max , 0.1 ) , np.arange ( y_min , y_max , 0.1 ) )
Z = np.dot ( np.c_ [ xx.ravel () , yy.ravel () ], w ) - b
Z = np.sign ( Z ).reshape ( xx.shape )
plt.contourf ( xx , yy , Z , alpha = 0.3 )
plt.show ()