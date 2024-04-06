#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 32/60 Funciones de Activación

import numpy as np
import matplotlib.pyplot as plt

#Definimos la función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#Definimos la función de activación tangente hiperbólica (tanh)
def tanh(x):
    return np.tanh(x)

#Creamos un rango de valores de entrada
x = np.linspace(-5, 5, 100)

#Calculamos los valores de salida para ambas funciones de activación
y_sigmoid = sigmoid(x)
y_tanh = tanh(x)

#Creamos un gráfico para visualizar las funciones de activación
plt.figure(figsize=(10, 6))

#Graficamos la función sigmoide
plt.plot(x, y_sigmoid, label='Sigmoide', color='blue')
#Añadimos etiquetas y título para mostrarlo al usuario
plt.xlabel('x')
plt.ylabel('y')
plt.title('Función de Activación - Sigmoide')
#Añadimos una leyenda
plt.legend()
#Mostramos la cuadrícula
plt.grid(True)

#Graficamos la función tangente hiperbólica (tanh)
plt.plot(x, y_tanh, label='Tanh', color='red')
#Añadimos etiquetas y título para mostrarlo al usuario
plt.xlabel('x')
plt.ylabel('y')
plt.title('Función de Activación - Tangente Hiperbólica')
#Añadimos una leyenda
plt.legend()
#Mostramos la cuadrícula
plt.grid(True)

#Mostramos el gráfico al usuario
plt.show()

