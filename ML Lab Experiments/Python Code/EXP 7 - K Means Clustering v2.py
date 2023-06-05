import math

def calculateEuclideanDistance ( point , center ) :
    return round ( math.sqrt ( ( point [ 0 ] - center [ 0 ] ) ** 2 + ( point [ 1 ] - center [ 1 ] ) ** 2 ) , 3 )

def executeIteration ( call , prev_clusters ) :
    centroids , distances , clusters , start = [] , [] , [ [] for i in range ( K ) ] , K if call == 1 else 0
    if call == 1 :
        for cind in range ( K ) :
            centroids.append ( inputs [ cind ] )
            clusters [ cind ].append ( inputs [ cind ] )
    else :
        for lst in prev_clusters :
            x , y = 0 , 0
            lng = len ( lst )
            for point in lst :
                x , y = x + point [ 0 ] , y + point [ 1 ]
            centroids.append ( [ round ( x / lng , 3 ) , round ( y / lng , 3 ) ] )
    print ( "\n Centroids = " , centroids )
    for ind in range ( start , len ( inputs ) ) :
        for center in range ( K ) :
            distances.append ( calculateEuclideanDistance ( inputs [ ind ] , centroids [ center ] ) )
        id = distances.index ( min ( distances ) )
        clusters [ id ].append ( inputs [ ind ] )
        distances.clear ()
    for cl in clusters :
        print ( cl )
    if call != 1 and prev_clusters == clusters :
        return False , prev_clusters
    prev_clusters = clusters
    return True , prev_clusters

def KmeansCluster () :
    itr , cont , prev_clusters = 1 , True , []
    while cont == True :
        cont , prev_clusters = executeIteration ( itr , prev_clusters )
        itr += 1
    print ( "\n Hence clusters in Iterations" , itr - 2 , "and" , itr - 1 , "match !")

print ( "\n Enter the values of K and no. of input samples : " )
K , n_input = map ( int , input ().split () )
inputs = []
print ( "\n Enter the values of input sample pairs : " )
for el in range ( n_input ) :
    inputs.append ( list ( map ( float , input ().split () ) ) )
KmeansCluster ()