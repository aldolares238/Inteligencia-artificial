#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 42/60 Recuperacion de datos

import matplotlib.pyplot as plt
import numpy as np

#Declaramos una funcion para simular la recuperacion de datos
def recuperacion_datos(prob_exito, intentos):
    prob_recuperacion = []
    for i in range(1, intentos + 1):
        #Generamos un número aleatorio entre 0 y 1 para determinar si se logra recuperar los datos en este intento.
        if np.random.rand() < prob_exito:
            prob_recuperacion.append(1)  #Éxito en la recuperación de datos
        else:
            prob_recuperacion.append(0)  #Fracaso en la recuperación de datos
    return prob_recuperacion

#Declaramos los Parámetros
prob_exito = 0.8  #Probabilidad de éxito en la recuperación de datos
intentos = 10  #Número de intentos

#Simulamos la recuperación de datos
prob_recuperacion = recuperacion_datos(prob_exito, intentos)

#Calculamos la probabilidad acumulada de recuperación en cada intento
prob_acumulada = [sum(prob_recuperacion[:i]) / i for i in range(1, intentos + 1)]

#Graficamos la probabilidad de recuperación en función de los intentos
plt.plot(range(1, intentos + 1), prob_acumulada, marker='o')
plt.xlabel('Número de Intentos')
plt.ylabel('Probabilidad de Recuperación')
plt.title('Probabilidad de Recuperación de Datos en función de los Intentos')
plt.grid(True)
plt.show()
