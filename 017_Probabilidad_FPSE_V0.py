#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 17/60  Filtrado, Predicción, Suavizado y Explicación

import numpy as np
import matplotlib.pyplot as plt

#Inicialización
#Estado inicial: posición y velocidad
x0 = 0
v0 = 1

#Definimos la Matriz de estado inicial
x = np.array([[x0],  #Posición inicial
              [v0]]) # elocidad inicial

#Definimos la Matriz de covarianza del estado inicial
P = np.diag([1, 1])

#Definimos la Matriz de transición de estado (determina cómo evoluciona el estado en el tiempo)
F = np.array([[1, 1],  #Posición = Posición anterior + Velocidad * Δt
              [0, 1]]) #Velocidad no cambia

#Definimos la Matriz de observación (determina cómo se relaciona el estado con las observaciones)
H = np.array([[1, 0]])  #Solo podemos observar la posición, no la velocidad

#Covarianza del ruido del proceso (ruido en la evolución del estado)
Q = np.diag([0.1, 0.1])

#Covarianza del ruido de la medición (ruido en las observaciones)
R = np.array([[0.5]])

# Paso 2: Predicción y actualización

# Parámetro de tiempo
dt = 1

#Señalamos un Número de muestras
n_samples = 50

#Lista para almacenar las estimaciones de posición
estimations = []

for i in range(n_samples):
    #Predicción del estado
    x_pred = np.dot(F, x)
    #Predicción de la covarianza del estado
    P_pred = np.dot(np.dot(F, P), F.T) + Q

    #Simulación de la observación (posición verdadera + ruido)
    z = np.array([[i + np.random.randn() * 0.5]])

    #Actualización del estado basada en la observación
    y = z - np.dot(H, x_pred)
    S = np.dot(np.dot(H, P_pred), H.T) + R
    K = np.dot(np.dot(P_pred, H.T), np.linalg.inv(S))
    x = x_pred + np.dot(K, y)
    P = P_pred - np.dot(np.dot(K, H), P_pred)

    #Guardar la estimación de la posición
    estimations.append(x[0, 0])

#Visualización de los resultados
plt.plot(range(n_samples), estimations, label='Estimación')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Filtro de Kalman: Estimación de Posición')
plt.legend()
plt.grid(True)
plt.show()
