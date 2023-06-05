import numpy as np

def calculateStep ( x1 , x2 , w1 , w2 , theta ) :
    z = x1 * w1 + x2 * w2 - theta
    return 1 if z >= 0 else 0

def updateWeights ( alpha , error , x1 , x2 , w1 , w2 ) :
    w1 += alpha * error * x1
    w2 += alpha * error * x2
    return w1 , w2

def calculateEpoch ( truth_table , w1 , w2 , alpha , theta ) :
    errors = []
    print ( " x1 \tx2  \tError \t w1  \t w2" )
    for row in truth_table :
        x1 , x2 , expected = row
        y = calculateStep ( x1 , x2 , w1 , w2 , theta )
        error = expected - y
        if error != 0 :
            w1 , w2 = updateWeights ( alpha , error , x1 , x2 , w1 , w2 )
        errors.append ( error )
        print ( " " , x1 , " \t" , x2 , " \t" , error , " \t" , w1 , " \t" , w2 )
    return w1 , w2 , errors

def calculatePerceptron ( gate , w1 , w2 , alpha , theta ) :
    if gate == "AND" :
        truth_table = np.array ( [ [ 0 , 0 , 0 ] , [ 0 , 1 , 0 ] , [ 1 , 0 , 0 ] , [ 1 , 1 , 1 ] ] )
    elif gate == "OR" :
        truth_table = np.array ( [ [ 0 , 0 , 0 ] , [ 0 , 1 , 1 ] , [ 1 , 0 , 1 ] , [ 1 , 1 , 1 ] ] )
    else:
        print ( "INVALID Gate !" )
        return
    epoch = 0
    while True :
        epoch += 1
        print ( "\n EPOCH " , epoch )
        w1 , w2 , errors = calculateEpoch ( truth_table , w1 , w2 , alpha , theta )
        if errors.count ( 0 ) == len ( errors ) :
            break
    print ( "\n Final Weights : w1 = {:.2f} , w2 = {:.2f}".format ( w1 , w2 ) )

print ( "\n Single Layer Perceptron - AND Gate" )
calculatePerceptron ( "AND" , 0.3 , -0.2 , 0.2 , 0.4 )