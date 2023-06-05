import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
#df = pd.read_csv(r"/content/PCA.csv")
#X_d = df['X'].values
#Y_d = df['Y'].values
X_d = [2,3,4,5,6,7]
Y_d = [1,5,3,6,7,8]
data = np.array([[X_d[i], Y_d[i]] for i in range(len(list(X_d)))])

mean = np.mean(data, axis=0)
centered_data = data - mean
covariance_matrix = np.cov(centered_data.T)
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]
print("Eigen Values : \n",eigenvalues)
print("Eigen Vectors : \n",eigenvectors)
k = 1

projection_matrix = eigenvectors[:, :k]
projected_data = np.dot(centered_data, projection_matrix)
pcaMatrix_rounded = np.round(projected_data, 3) 
print("Original Data:\n", data)
print("Projected Data:\n", pcaMatrix_rounded)

# Plot the original data and the projected data
plt.scatter(data[:, 0], data[:, 1], alpha=0.3, label='Original data')
plt.scatter(projected_data[:, 0], np.zeros(len(projected_data)), alpha=0.8, label='Projected data')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
