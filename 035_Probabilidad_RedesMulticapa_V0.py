#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 35/60 Redes Multicapa

import numpy as np
import matplotlib.pyplot as plt

#Definimos la función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#Declaramos los Datos de entrada
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

#Declaramos las Etiquetas de salida 
y = np.array([[0],
              [1],
              [1],
              [0]])

#Inicializamos los parámetros de la red neuronal
input_size = 2
hidden_size = 4
output_size = 1

#Declaramos los Pesos para la capa oculta y la capa de salida (inicializados aleatoriamente)
weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))
weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))

#Propagación hacia adelante
hidden_layer_input = np.dot(X, weights_input_hidden)
hidden_layer_output = sigmoid(hidden_layer_input)

output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
output_layer_output = sigmoid(output_layer_input)

#Visualización de los resultados
plt.scatter(X[:,0], X[:,1], c=output_layer_output.flatten(), cmap='viridis')
plt.title('Resultado de la red neuronal')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Salida de la red neuronal')
plt.show()
