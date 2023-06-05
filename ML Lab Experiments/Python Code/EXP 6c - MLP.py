import math

def updateWeightsAndBiases () :
    for ip in range ( 1 , n_input + 1 ) :
        for hid in range ( n_input + 1 , n_input + n_hidden + 1 ) :
            inputs [ "w" + str ( ip ) + str ( hid ) ] += round ( alpha * inputs [ "Error" + str ( hid ) ] * inputs [ "O" + str ( ip ) ] , 3 )
    for hid in range ( n_input + 1 , n_input + n_hidden + 1 ) :
        inputs [ "theta" + str ( hid ) ] += round ( alpha * inputs [ "Error" + str ( hid ) ] , 3 )
        for op in range ( n_input + n_hidden + 1 , n_input + n_hidden + n_output + 1 ) :
            inputs [ "w" + str ( hid ) + str ( op ) ] += round ( alpha * inputs [ "Error" + str ( op ) ] * inputs [ "O" + str ( hid ) ] , 3 ) 
    for op in range ( n_input + n_hidden + 1 , n_input + n_hidden + n_output + 1 ) :
        inputs [ "theta" + str ( op ) ] += round ( alpha * inputs [ "Error" + str ( op ) ] , 3 )

def forwardPropagation ( call ) :
    for op in range ( n_input + n_hidden + 1 , n_input + n_hidden + n_output + 1 ) :
        inputs [ "I" + str ( op ) ] = inputs [ "theta" + str ( op ) ]
        for hid in range ( n_input + 1 , n_input + n_hidden + 1 ) :
            inputs [ "I" + str ( hid ) ] = round ( inputs [ "theta" + str ( hid ) ] , 3 )
            for inp in range ( 1 , n_input + 1 ) :
                inputs [ "I" + str ( hid ) ] += round ( inputs [ "x" + str ( inp ) ] * inputs [ "w" + str ( inp ) + str ( hid ) ] , 3 )
            inputs [ "O" + str ( hid ) ] = round ( 1 / ( 1 + math.exp ( - inputs [ "I" + str ( hid ) ] ) ) , 3 )
            inputs [ "I" + str ( op ) ] += round ( inputs [ "O" + str ( hid ) ] * inputs [ "w" + str ( hid ) + str ( op ) ] , 3 )
        inputs [ "O" + str ( op ) ] = round ( 1 / ( 1 + math.exp ( - inputs [ "I" + str ( op ) ] ) ) , 3 )
        inputs [ "Error" + str ( op ) ] = round ( inputs [ "Odes" + str ( op ) ] - inputs [ "O" + str ( op ) ] , 3 )
        inputs [ str ( call ) + "Error" + str ( op ) ] = inputs [ "Error" + str ( op ) ]

def backwardPropagation () :
    for op in range ( n_input + n_hidden + 1 , n_input + n_hidden + n_output + 1 ) :
        O_op = inputs [ "O" + str ( op ) ]
        inputs [ "Error" + str ( op ) ] = round ( O_op * ( 1 - O_op ) * ( inputs [ "Odes" + str ( op ) ] - O_op ) , 3 )
    for hid in range ( n_input + 1 , n_input + n_hidden + 1 ) :
        O_hid = inputs [ "O" + str ( hid ) ]
        inputs [ "Error" + str ( hid ) ] = round ( O_hid * ( 1 - O_hid ) , 3 )
        err_wt = 0
        for op in range ( n_input + n_hidden + 1 , n_input + n_hidden + n_output + 1 ) :
            err_wt += inputs [ "Error" + str ( op ) ] * inputs [ "w" + str ( hid ) + str ( op ) ]
        inputs [ "Error" + str ( hid ) ] *= round ( err_wt , 3 )
    updateWeightsAndBiases ()

def calculateMLP () :
    print ( "\n\n ITERATION 1\n\n Forward Propagation ..." )
    forwardPropagation ( 1 )
    backwardPropagation ()
    print ( "\n Backward Propagation ...\n\n" ) #, inputs )
    print ( " ITERATION 2\n\n Forward Propagation ..." )
    forwardPropagation ( 2 )
    for op in range ( n_input + n_hidden + 1 , n_input + n_hidden + n_output + 1 ) :
        err1 , err2 = inputs [ "1Error" + str ( op ) ] , inputs [ "2Error" + str ( op ) ]
        print ( "\n ITERATION 1 Error at Ouput Node " , op , " = " , err1 )
        print ( "\n ITERATION 2 Error at Ouput Node " , op , " = " , err2 )
        print ( "\n Therefore using MLP , Error reduced = " , round ( err1 - err2 , 3 ) )

alpha = 0.8
n_input , n_hidden , n_output = 4 , 2 , 1
inputs = { "x1" : 1 , "x2" : 1 , "x3" : 0 , "x4" : 1 ,
"w15" : 0.3 , "w16" : 0.1 , "w25" : -0.2 , "w26" : 0.4 , "w35" : 0.2 , "w36" : -0.3 , 
"w45" : 0.1 , "w46" : 0.4 , "w57" : -0.3 , "w67" : 0.2 ,
"O1" : 1 , "O2" : 1 , "O3" : 0 , "O4" : 1 , "Odes7" : 1 ,
"theta5" : 0.2 , "theta6" : 0.1 , "theta7" : -0.3
}

counter = 0
for key , value in inputs.items () :
    if counter % 5 == 0 :
        print ()
    print ( key , '=' , value , end = ' , ' )
    counter += 1

calculateMLP ()

"""
inputs = {}
alpha = float ( input ( "\n Enter the learning rate ( alpha ) : " ) )
print ( "\n Enter the no. of neurons in the input , hidden and output layers respectively" )
n_input , n_hidden , n_output = map ( int , input ().split () )
print ( "\n Enter Input samples ( x ) , weights ( w ) , bias ( theta ) and desired output ( Odes ) values" )
for i in range ( 1 , n_input + 1 ) :
    inputs [ "x" + str ( i ) ] = int ( input ( " x" + str ( i ) + " : " ) )
    inputs [ "O" + str ( i ) ] = inputs [ "x" + str ( i ) ]
    for h in range ( n_input + 1 , n_input + n_hidden + 1 ) :
        inputs [ "w" + str ( i ) + str ( h ) ] = float ( input ( " w" + str ( i ) + str ( h ) + " : " ) )
for h in range ( n_input + 1 , n_input + n_hidden + 1 ) :
    inputs [ "theta" + str ( h ) ] = float ( input ( " theta" + str ( h ) + " : " ) )
    for o in range ( n_input + n_hidden + 1 , n_input + n_hidden + n_output + 1 ) :
        inputs [ "w" + str ( h ) + str ( o ) ] = float ( input ( " w" + str ( h ) + str ( o ) + " : " ) )
for o in range ( n_input + n_hidden + 1 , n_input + n_hidden + n_output + 1 ) :
    inputs [ "theta" + str ( o ) ] = float ( input ( " theta" + str ( o ) + " : " ) )
    inputs [ "Odes" + str ( o ) ] = int ( input ( " Odes" + str ( o ) + " : " ) )
calculateMLP ()
"""