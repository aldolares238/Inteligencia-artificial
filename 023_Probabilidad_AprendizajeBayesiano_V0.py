#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 23/60 Aprendizaje Bayesiano

import numpy as np
import matplotlib.pyplot as plt

#Creamos datos de entrenamiento sintéticos
#Supongamos que estamos clasificando elementos como "A" o "B" basados en dos características
#Los datos están distribuidos normalmente alrededor de dos centroides

#Media y desviación estándar de las características para la clase "A"
mean_A = [1, 1]
cov_A = [[1, 0.5], [0.5, 1]]

#Media y desviación estándar de las características para la clase "B"
mean_B = [4, 4]
cov_B = [[1, -0.5], [-0.5, 1]]

#Generamos datos de entrenamiento para ambas clases
data_A = np.random.multivariate_normal(mean_A, cov_A, 100)
data_B = np.random.multivariate_normal(mean_B, cov_B, 100)

#Graficamos los datos de entrenamiento
plt.scatter(data_A[:, 0], data_A[:, 1], label='Clase A')
plt.scatter(data_B[:, 0], data_B[:, 1], label='Clase B')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.title('Datos de entrenamiento')
plt.legend()
plt.show()

#Ahora, supongamos que tenemos un nuevo punto que queremos clasificar
new_point = np.array([2, 3])

#Calculamos la probabilidad a priori de cada clase
prior_A = len(data_A) / (len(data_A) + len(data_B))
prior_B = len(data_B) / (len(data_A) + len(data_B))

#Calculamos las probabilidades condicionales de que el nuevo punto pertenezca a cada clase
likelihood_A = (1 / (2 * np.pi * np.linalg.det(cov_A) ** 0.5)) * np.exp(-0.5 * np.dot(np.dot((new_point - mean_A), np.linalg.inv(cov_A)), (new_point - mean_A).T))
likelihood_B = (1 / (2 * np.pi * np.linalg.det(cov_B) ** 0.5)) * np.exp(-0.5 * np.dot(np.dot((new_point - mean_B), np.linalg.inv(cov_B)), (new_point - mean_B).T))

#Calculamos la probabilidad posterior de cada clase usando el teorema de Bayes
posterior_A = (likelihood_A * prior_A) / (likelihood_A * prior_A + likelihood_B * prior_B)
posterior_B = (likelihood_B * prior_B) / (likelihood_A * prior_A + likelihood_B * prior_B)

#Clasificamos el nuevo punto según la probabilidad posterior
if posterior_A > posterior_B:
    print("El nuevo punto pertenece a la clase A")
else:
    print("El nuevo punto pertenece a la clase B")

#Graficamos el nuevo punto junto con las regiones de decisión
plt.scatter(data_A[:, 0], data_A[:, 1], label='Clase A')
plt.scatter(data_B[:, 0], data_B[:, 1], label='Clase B')
plt.scatter(new_point[0], new_point[1], color='red', label='Nuevo punto')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')

#Dibujamos las regiones de decisión
x = np.linspace(-1, 6, 100)
y = np.linspace(-1, 6, 100)
X, Y = np.meshgrid(x, y)
Z_A = np.zeros_like(X)
Z_B = np.zeros_like(X)
for i in range(len(x)):
    for j in range(len(y)):
        point = np.array([x[i], y[j]])
        likelihood_A = (1 / (2 * np.pi * np.linalg.det(cov_A) ** 0.5)) * np.exp(-0.5 * np.dot(np.dot((point - mean_A), np.linalg.inv(cov_A)), (point - mean_A).T))
        likelihood_B = (1 / (2 * np.pi * np.linalg.det(cov_B) ** 0.5)) * np.exp(-0.5 * np.dot(np.dot((point - mean_B), np.linalg.inv(cov_B)), (point - mean_B).T))
        posterior_A = (likelihood_A * prior_A) / (likelihood_A * prior_A + likelihood_B * prior_B)
        posterior_B = (likelihood_B * prior_B) / (likelihood_A * prior_A + likelihood_B * prior_B)
        Z_A[j, i] = posterior_A
        Z_B[j, i] = posterior_B
plt.contour(X, Y, Z_A, levels=[0.5], colors='blue', alpha=0.5)
plt.contour(X, Y, Z_B, levels=[0.5], colors='green', alpha=0.5)

plt.title('Clasificación del nuevo punto')
plt.legend()
plt.show()

