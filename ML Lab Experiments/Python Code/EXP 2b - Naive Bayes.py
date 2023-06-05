import pandas as pd
import numpy as np

# Read the data from CSV file
data = pd.read_csv("nb_dataset.csv")
print("\nData read from nb_dataset.csv:\n\n", data)

# Convert data into a numpy array
arr = np.array(data)
print("\nNumpy array:\n", arr)

# Split data into input features and target variable
X = arr[:, :-1]
y = arr[:, -1]

# Create a list of unique values for each attribute , 4 - columns
iters = [arr[:, x] for x in range(4)]
attr_labels = [list(set(itr)) for itr in iters]
print(attr_labels)

# Compute the conditional probabilities
def computeTable(iters, attr_labels):
    matrix = []
    for itr, attr_label in zip(iters, attr_labels):
        mtx = {x: [0 for y in range(2)] for x in attr_label}
        for el in range(len(itr)):
            for lb in attr_label:
                if itr[el] == lb:
                    if y[el] == "Yes":
                        mtx[lb][0] += 1
                    else:
                        mtx[lb][1] += 1
        matrix.append(mtx)
    return matrix

mtcs = computeTable(iters, attr_labels)
print("\nConditional probabilities:\n", mtcs)

# Calculate the prior probabilities
targets = [0, 0]
for el in y:
    if el == "Yes":
        targets[0] += 1
    else:
        targets[1] += 1
targets = [target / sum(targets) for target in targets]
print("\nPrior probabilities: (A/A+B) \n", targets)

# Define attribute values for a new sample
today = ["Overcast", "Hot", "Normal", False]

# Calculate the posterior probabilities
def calcProbability(matrix, target):
    probs = [1, 1]
    for ind in range(len(matrix)):
        countYes = matrix[ind][today[ind]][0]
        countNo = matrix[ind][today[ind]][1]
        totalYes = sum([matrix[ind][x][0] for x in matrix[ind]])
        totalNo = sum([matrix[ind][x][1] for x in matrix[ind]])
        currProbs = [countYes / totalYes, countNo / totalNo]
        probs = [prob * currProb for prob, currProb in zip(probs, currProbs)]
    probs = [prob * trg for prob, trg in zip(probs, target)]
    return probs

result = calcProbability(mtcs, targets)
print("\nPosterior probabilities: (Result) \n", result)
