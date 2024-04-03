#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 20/60 Filtros de Kalman

import numpy as np
import matplotlib.pyplot as plt

#Definimos las matrices A y H para el sistema
A = np.array([[1, 1], [0, 1]])  #Matriz de transición de estado
H = np.array([[1, 0]])          #Matriz de observación

#Definimos las matrices de covarianza del proceso y de observación
Q = np.array([[0.1, 0], [0, 0.1]])  #Covarianza del proceso
R = np.array([[1]])                 #Covarianza de la medición

#Inicializamos el estado y la covarianza estimada
x_hat = np.array([[0], [0]])  #Estado inicial
P = np.eye(2)                 #Covarianza inicial

#Generamos datos simulados
np.random.seed(0)
true_state = np.zeros((2, 100))
measurements = np.zeros((1, 100))
for i in range(1, 100):
    true_state[:, i] = np.dot(A, true_state[:, i-1]) + np.random.multivariate_normal([0, 0], Q)
    measurements[:, i] = np.dot(H, true_state[:, i]) + np.random.normal(0, R[0, 0])

#Implementamos del filtro de Kalman
estimated_state = np.zeros((2, 100))
for i in range(1, 100):
    #Predicción del estado
    x_hat_minus = np.dot(A, x_hat)
    P_minus = np.dot(np.dot(A, P), A.T) + Q
    
    #Actualización basada en la medición
    K = np.dot(np.dot(P_minus, H.T), np.linalg.inv(np.dot(np.dot(H, P_minus), H.T) + R))
    x_hat = x_hat_minus + np.dot(K, (measurements[:, i] - np.dot(H, x_hat_minus)))
    P = np.dot((np.eye(2) - np.dot(K, H)), P_minus)
    
    estimated_state[:, i] = x_hat.flatten()

#Graficar resultados con colores y etiquetas para el usuario
plt.figure()
plt.plot(true_state[0, :], label='True State')
plt.plot(measurements.flatten(), 'rx', label='Measurements')
plt.plot(estimated_state[0, :], 'g--', label='Estimated State')
plt.legend()
plt.title('Filtro de Kalman - Estimación del estado')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.show()
