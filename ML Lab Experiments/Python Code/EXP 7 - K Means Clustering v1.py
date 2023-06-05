import numpy as np
import matplotlib.pyplot as plt

k = 3
X = np.array([[2, 10], [5, 8], [1, 2], [2, 5], [7, 5], [4, 9], [8, 4], [6, 4]])
centroids = X[np.random.choice(X.shape[0], size=k, replace=False)]
C = np.zeros(len(X))

old_centroids=0
while True:
    for i in range(len(X)):
        distances = np.linalg.norm(X[i] - centroids, axis=1)
        C[i] = np.argmin(distances)

    for j in range(k):
        centroids[j] = np.mean(X[C == j], axis=0)

    if np.allclose(centroids, old_centroids):
        break
    old_centroids = centroids.copy()

clusters = []
for j in range(k):
    clusters.append(X[C == j])

for j in range(k):
    print(f"Cluster {j+1}: {clusters[j]}")

colors = ['r', 'g', 'b']
for i in range(k):
    plt.scatter(X[C == i, 0], X[C == i, 1], c=colors[i])
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=300, c='black')
plt.show()
