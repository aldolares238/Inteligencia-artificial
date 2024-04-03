#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 25/60 Algoritmo EM

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

#Generamos datos de ejemplo con 2 clusters
X, y_true = make_blobs(n_samples=400, centers=2, cluster_std=0.60, random_state=0)
X = X[:, ::-1]  # Intercambiar las características para facilitar el trazado

#Visualizamos los datos de entrada
plt.scatter(X[:, 0], X[:, 1], s=40, cmap='viridis')
plt.title("Datos de entrada")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()

#Inicializamos el modelo GMM con 2 componentes
gmm = GaussianMixture(n_components=2, max_iter=20, random_state=0)

#Ajustamos el modelo a los datos
gmm.fit(X)

#Predecimos las asignaciones de cluster utilizando el modelo ajustado
labels = gmm.predict(X)

#Visualizamos los clusters encontrados por el algoritmo EM
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')
plt.title("Clusters encontrados por EM")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")

#Visualizamos los centros de los clusters
centers = gmm.means_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75)
plt.show()
