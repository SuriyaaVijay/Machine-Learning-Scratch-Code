import numpy as np
import pandas as pd

def LDA_fit ( X , y ) :
    n_features = X.shape [ 1 ]
    class_labels = np.unique ( y )
    mean_overall = np.mean ( X , axis = 0 )
    SW = np.zeros ( ( n_features , n_features ) )
    SB = np.zeros ( ( n_features , n_features ) )
    for clas in class_labels :
        X_cls = X [ y == clas ]
        mean_cls = np.mean ( X_cls , axis = 0 )
        SW += ( ( X_cls - mean_cls ).T).dot ( ( X_cls - mean_cls ) ).astype ( 'float64' )
        n_cls = X_cls.shape [ 0 ]
        mean_diff = ( mean_cls - mean_overall ).reshape ( n_features , 1 )
        SB += n_cls * ( ( mean_diff ).dot ( mean_diff.T ) ).astype ( 'float64' )
    A = np.linalg.inv ( SW ).dot ( SB )
    eigenvalues , eigenvectors = np.linalg.eig ( A )
    eigenvectors = eigenvectors.T
    idxs = np.argsort ( abs ( eigenvalues ) ) [ : : -1 ]
    eigenvalues = eigenvalues [ idxs ]
    eigenvectors = eigenvectors [ idxs ]
    linear_discriminants = eigenvectors [ 0 : n_components ]
    return linear_discriminants

data = pd.read_csv ( "lda_dataset.csv" )
print ( "\n Data read from dataset.csv :\n\n" , data )

arr = np.array ( data )
X = arr [ : , : -1 ]
y = arr [ : , -1 ]

n_components , linear_discriminants = 1 , None
linear_discriminants = LDA_fit ( X , y )
X_projected = np.dot ( X , linear_discriminants.T )
print ( "\n Linear Discriminants : " , linear_discriminants )
print ( "\n Shape of X : " , X.shape )
print ( "\n Shape of transformed X : " , X_projected.shape )