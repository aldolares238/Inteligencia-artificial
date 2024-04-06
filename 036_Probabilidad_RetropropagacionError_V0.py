#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 36/60 Retropropagación del Error

import numpy as np
import matplotlib.pyplot as plt

#Definimos la función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#Aplicamos la Derivada de la función de activación sigmoide
def sigmoid_derivative(x):
    return x * (1 - x)

#Declaramos los Datos de entrada
input_data = np.array([[0, 0],
                       [0, 1],
                       [1, 0],
                       [1, 1]])

#Declaramos Resultados esperados
expected_output = np.array([[0],
                            [1],
                            [1],
                            [0]])

#Configuración de la arquitectura de la red neuronal
input_neurons = 2
hidden_neurons = 4
output_neurons = 1
learning_rate = 0.1
epochs = 10000

#Inicializamos los pesos aleatorios para las conexiones de la red
hidden_weights = np.random.uniform(size=(input_neurons, hidden_neurons))
output_weights = np.random.uniform(size=(hidden_neurons, output_neurons))

#Declaramos la Lista para almacenar errores durante el entrenamiento
error_list = []

#Entrenamiento de la red neuronal mediante retropropagación del error
for epoch in range(epochs):
    #Forward Propagation
    hidden_activation = sigmoid(np.dot(input_data, hidden_weights))
    output_activation = sigmoid(np.dot(hidden_activation, output_weights))

    #Cálculo del error
    error = expected_output - output_activation
    error_list.append(np.mean(np.abs(error)))

    #Backpropagation
    output_delta = error * sigmoid_derivative(output_activation)
    hidden_error = output_delta.dot(output_weights.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_activation)

    #Actualización de los pesos
    output_weights += hidden_activation.T.dot(output_delta) * learning_rate
    hidden_weights += input_data.T.dot(hidden_delta) * learning_rate

#Visualización del error a lo largo del entrenamiento
plt.plot(error_list)
plt.xlabel('Epochs')
plt.ylabel('Error')
plt.title('Training Error')
plt.show()

#Mostrar resultado final
print("Resultado después del entrenamiento:")
print(output_activation)


