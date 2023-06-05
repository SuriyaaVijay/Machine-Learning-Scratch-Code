import pandas as pd
import numpy as np
import math
from tabulate import tabulate

def computeWeightedError ( ds_table ) :
    wError = sum ( ds_table [ ds_table [ 'Actual' ] != ds_table [ 'Predicted' ] ] [ 'Weight' ] )
    print ( "\n Weighted Error = ", wError )
    return wError

def computeWeightOfWeakClassifier ( wError ) :
    alpha = 0.5 * math.log ( ( 1 - wError ) / wError ) if wError != 0 else 0
    print ( "\n Alpha = ", alpha )
    return alpha

def computeNormalizingFactor ( ds_table , alpha ) :
    Z = 0
    correct_weight = ds_table [ ds_table [ 'Actual' ] == ds_table [ 'Predicted' ] ] [ 'Weight' ].unique ()
    incorrect_weight = ds_table [ ds_table [ 'Actual' ] != ds_table [ 'Predicted' ] ] [ 'Weight' ].unique ()
    for weight in correct_weight :
        crct_table = ds_table [ ds_table [ 'Actual' ] == ds_table [ 'Predicted' ] ]
        crct_count = len ( crct_table [ crct_table [ 'Weight' ] == weight ] )
        Z += ( weight * crct_count * math.exp ( -alpha ) )
    for weight in incorrect_weight :
        incrct_table = ds_table [ ds_table [ 'Actual' ] != ds_table [ 'Predicted' ] ]
        incrct_count = len ( incrct_table [ incrct_table [ 'Weight' ] == weight ] )
        Z += ( weight * incrct_count * math.exp ( alpha ) )
    print ( "\n Normalizing Factor = ", Z )
    return Z

def updateWeights ( ds_table , alpha , Z ) :
    ds_table.loc [ ds_table [ 'Actual' ] == ds_table [ 'Predicted' ] , 'Weight' ] *= math.exp ( -alpha ) / Z
    ds_table.loc [ ds_table [ 'Actual' ] != ds_table [ 'Predicted' ] , 'Weight' ] *= math.exp ( alpha ) / Z
    return ds_table

def decisionStump ( X , y , attribute , weights ) :
    ds_table = pd.DataFrame({attribute: X[attribute], 'Actual': y, 'Weight': weights})
    pos_class = input(f"\n Enter the desired attribute class for positive instance under '{attribute}': ")
    ds_table[attribute] = ds_table[attribute].astype(type(pos_class))
    ds_table['Predicted'] = np.where( ds_table[attribute] == pos_class, "Yes", "No" )
    print ( "\n Decision Stump Table : \n" , tabulate ( ds_table , headers = 'keys' , tablefmt = 'psql' ) )
    wError = computeWeightedError(ds_table)
    alpha = computeWeightOfWeakClassifier(wError)
    Z = computeNormalizingFactor(ds_table, alpha)
    ds_table = updateWeights(ds_table, alpha, Z)
    return pos_class , ds_table, alpha, Z

def computeWeightedPredictionAverage(X_train, alphas, attribute_classes ):
    weighted_predictions = np.zeros(X_train.shape[0])
    for ind in X_train.index :
        weighted_pred = 0
        for attribute in attribute_classes :
            if alphas[attribute] != 0 :
                pred = 1 if str (X_train[attribute][ind]) == attribute_classes[attribute] else 0
                weighted_pred += alphas[attribute] * pred
        weighted_predictions [ ind ] = weighted_pred
    print ( "\n Weighted Predictions = " , weighted_predictions )  
    return weighted_predictions

def makePrediction(X_train, ds_tables, alphas, attribute_classes ):
    table_attributes = ["alpha_" + attr + " = " + str ( round ( alphas [ attr ] , 3 ) ) for attr in alphas ]
    prediction_table = pd.DataFrame(columns=table_attributes + ['Weighted Average', 'Final Prediction'])
    weighted_avgs = computeWeightedPredictionAverage(X_train, alphas, attribute_classes )
    prediction_table['Weighted Average'] = weighted_avgs
    prediction_table['Final Prediction'] = np.where(weighted_avgs > 0, "Yes", "No")
    for attr in alphas :
        prediction_table [ "alpha_" + attr + " = " + str ( round ( alphas [ attr ] , 3 ) ) ] = ds_tables [attr]['Predicted']
    print ("\n Final Prediction Table : \n\n" , tabulate ( prediction_table , headers = 'keys' , tablefmt = 'psql' ) )
    return prediction_table

def adaBoost(X_train, y_train):
    X_train = pd.DataFrame(X_train, columns=data.columns[:-1])
    weights , alphas , ds_tables , attribute_classes = np.ones(len(X_train)) / len(X_train) , {} , {} , {}
    for attribute in X_train.columns:
        pos_class , ds_table , alpha , Z = decisionStump(X_train, y_train, attribute, weights)
        weights = ds_table [ 'Weight']
        if alpha != 0 :
            ds_tables [ attribute ] = ds_table
            attribute_classes [ attribute ] = pos_class
            alphas [ attribute ] = alpha
    pred_table = makePrediction (X_train, ds_tables , alphas , attribute_classes )
    tabulate ( pred_table , headers = 'keys' , tablefmt = 'psql' )

data = pd.read_csv ( "adaBoost.csv" )
print ( "\n" , data , "\n" )
arr = np.array ( data )
X = arr [ : , : -1 ]
y = arr [ : , -1 ]
adaBoost ( X , y )