import matplotlib.pyplot as plt
import numpy as np

x_coord = np.random.randint ( 10 , size = 5 )
y_coord = np.random.randint ( 0 , 100 , size = 5 )
print ( x_coord , y_coord )

plt.plot ( x_coord , y_coord )
plt.xlabel ( "Random Weights" )
plt.ylabel ( "Scores" )
plt.show ()