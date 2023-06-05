import pandas as pd
import numpy as np

def calculate_Slope ( x , y , n ) :
    numerator = ( n * np.sum ( x * y ) ) - ( np.sum ( x ) * np.sum ( y ) )
    denominator = ( n * np.sum ( x ** 2 ) ) - ( np.sum ( x ) ** 2 )
    return numerator / denominator

def calculate_Y_Intercept ( x , y , m , n ) :
    return ( np.sum ( y ) - ( m * np.sum ( x ) ) ) / n

def evaluate_Model ( df ) :
    n = len ( df )
    x = df [ df.columns [ 0 ] ]
    y = df [ df.columns [ 1 ] ]
    y_mean = np.mean ( y )
    m = round ( calculate_Slope ( x , y , n ) , 2 )
    c = round ( calculate_Y_Intercept ( x , y , m , n ) , 2 )
    df [ 'y_cap' ] = m * x + c
    SSR = round ( np.sum ( ( df [ 'y_cap' ] - y_mean ) ** 2 ) , 3 )
    SST = round ( np.sum ( ( y - y_mean ) ** 2 ) , 3 )
    SSE = round ( np.sum ( ( y - df [ 'y_cap' ] ) ** 2 ) , 3 )
    R_squared = round ( SSR / SST , 3 )
    return m , c , SSR , SST , SSE , R_squared

data = pd.read_csv ( 'LR_dataset.csv' )
print ( "\n Data read from dataset.csv :\n\n" , data )
df = pd.DataFrame ( data )
m , c , SSR , SST , SSE , R_squared = evaluate_Model ( df )
print ( "\n Linear Regression equation : y = (" , m , ") x + (" , c , ")" )
print ( "\n Sum of Squares Total ( SST ) = " , SST )
print ( " Sum of Squares Regression ( SSR ) = " , SSR )
print ( " Sum of Squares Error ( SSE ) = " , SSE )
print ( " R-squared = " , R_squared )