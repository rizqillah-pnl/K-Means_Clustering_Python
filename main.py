# Three lines to make our compiler able to draw:
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


x = [2, 3, 2, 2, 1, 3, 4, 6, 5, 4]
y = [1, 2, 2, 3, 3, 1, 2, 3, 4, 4]

data = list(zip(x, y))

kmeans = KMeans(n_clusters=4)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.show()


inertias = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1, 11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()
