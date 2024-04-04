#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 26/60 Agrupamiento No Supervisado

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Generamos datos aleatorios para el ejemplo
np.random.seed(0)
X = np.random.randn(100, 2) * 2 + np.array([2, 2])

#Visualizamos los datos generados antes del proceso
plt.scatter(X[:,0], X[:,1], s=50, alpha=0.5)
plt.title('Datos Aleatorios')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

#Definimos el número de clusters (grupos) que queremos encontrar
n_clusters = 3

#Inicializamos el modelo KMeans con el número de clusters
kmeans = KMeans(n_clusters=n_clusters)

#Ajusstamos el modelo a los datos
kmeans.fit(X)

#Obtenemos los centroides de los clusters encontrados
centroids = kmeans.cluster_centers_

#Obtenemos las etiquetas de los clusters para cada punto
labels = kmeans.labels_

#Visualizamos los clusters y sus centroides de manera grafica para el usuario
colors = ['r', 'g', 'b']
plt.figure()
for i in range(n_clusters):
    plt.scatter(X[labels == i][:,0], X[labels == i][:,1], s=50, c=colors[i], alpha=0.5, label=f'Cluster {i+1}')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='k', label='Centroides')
plt.title('Agrupamiento con KMeans')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
