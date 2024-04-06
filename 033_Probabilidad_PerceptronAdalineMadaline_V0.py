#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 33/60 Perceptrón, ADALINE y MADALINE

import numpy as np
import matplotlib.pyplot as plt

#Declaramos la Función para generar datos de ejemplo
def generar_datos(num_muestras, num_caracteristicas):
    #Generamos valores aleatorios para las características
    X = np.random.rand(num_muestras, num_caracteristicas)
    #Generamos etiquetas de clase aleatorias (0 o 1)
    y = np.random.randint(0, 2, size=num_muestras)
    return X, y

#Declaramos una Función para visualizar los datos
def visualizar_datos(X, y, titulo):
    plt.figure()
    plt.title(titulo)
    #Graficamos los puntos de clase 0 en azul
    plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='blue', label='Clase 0')
    #Graficamos los puntos de clase 1 en rojo
    plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='red', label='Clase 1')
    plt.legend()
    plt.xlabel('Característica 1')
    plt.ylabel('Característica 2')

#Declaramos la Función de activación (escalón)
def funcion_activacion(z):
    return np.where(z >= 0, 1, 0)

#Declaramos el Algoritmo del perceptrón
def perceptron(X, y, num_iteraciones):
    num_muestras, num_caracteristicas = X.shape
    #Inicializamos los pesos aleatorios
    pesos = np.random.rand(num_caracteristicas)
    for _ in range(num_iteraciones):
        for i in range(num_muestras):
            #Producto punto entre características y pesos
            z = np.dot(X[i], pesos)
            #Función de activación
            prediccion = funcion_activacion(z)
            #Actualización de pesos
            delta = y[i] - prediccion
            pesos += delta * X[i]
    return pesos

#Declaramos el Algoritmo ADALINE
def adaline(X, y, tasa_aprendizaje, num_iteraciones):
    num_muestras, num_caracteristicas = X.shape
    #Inicialización de pesos aleatorios
    pesos = np.random.rand(num_caracteristicas)
    for _ in range(num_iteraciones):
        for i in range(num_muestras):
            #Producto punto entre características y pesos
            z = np.dot(X[i], pesos)
            #Función de activación
            prediccion = funcion_activacion(z)
            #Actualización de pesos según la regla del perceptrón
            delta = y[i] - z
            pesos += tasa_aprendizaje * delta * X[i]
    return pesos

#Algoritmo MADALINE
def madaline(X, y, tasa_aprendizaje, num_iteraciones):
    num_muestras, num_caracteristicas = X.shape
    #Inicialización de pesos aleatorios
    pesos = np.random.rand(num_caracteristicas)
    for _ in range(num_iteraciones):
        for i in range(num_muestras):
            #Producto punto entre características y pesos
            z = np.dot(X[i], pesos)
            #Función de activación
            prediccion = funcion_activacion(z)
            #Actualización de pesos según la regla del perceptrón
            delta = y[i] - z
            pesos += tasa_aprendizaje * delta * X[i]
    return pesos

#Generamos datos de ejemplo
X, y = generar_datos(100, 2)

#Visualizamos datos de ejemplo
visualizar_datos(X, y, 'Datos de ejemplo')

#Ejecutamos el perceptrón
pesos_perceptron = perceptron(X, y, num_iteraciones=100)

#Ejecutamos ADALINE
pesos_adaline = adaline(X, y, tasa_aprendizaje=0.1, num_iteraciones=100)

#Ejecutamos MADALINE
pesos_madaline = madaline(X, y, tasa_aprendizaje=0.1, num_iteraciones=100)

#Visualizamos las líneas de separación
x_values = np.linspace(0, 1, 100)
plt.plot(x_values, -(pesos_perceptron[0] * x_values) / pesos_perceptron[1], label='Perceptrón')
plt.plot(x_values, -(pesos_adaline[0] * x_values) / pesos_adaline[1], label='ADALINE')
plt.plot(x_values, -(pesos_madaline[0] * x_values) / pesos_madaline[1], label='MADALINE')
plt.legend()
plt.show()
