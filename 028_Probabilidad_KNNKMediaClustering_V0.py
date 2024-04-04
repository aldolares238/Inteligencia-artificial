#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 28/60 k-NN, k-Medias y Clustering

# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier

# Generar datos aleatorios
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Mostrar los datos generados
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title('Datos Generados')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()

#Aplicamos el algoritmo K-Means para agrupar los datos
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
#Obtenemos los centroides de los grupos
centroids = kmeans.cluster_centers_
#Obtenemos las etiquetas de los grupos
labels = kmeans.labels_
#Mostramos los grupos encontrados por K-Means para el usuario
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='red', s=200)
plt.title('Grupos encontrados por K-Means')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()

#Aplicamos el algoritmo k-NN para clasificar los datos generados
knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(X, labels)

#Predecimos las etiquetas de los datos generados
new_data = np.array([[0, 2], [3, 2], [-3, -2], [6, 4]])
predicted_labels = knn.predict(new_data)

#Mostramos los datos generados junto con sus etiquetas predichas por k-NN
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(new_data[:, 0], new_data[:, 1], c=predicted_labels, marker='x', s=100, cmap='viridis')
plt.title('Clasificación de Nuevos Datos por k-NN')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()
