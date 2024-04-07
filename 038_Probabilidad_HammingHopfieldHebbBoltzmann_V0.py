#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 38/60 Hamming, Hopfield, Hebb, Boltzmann

import numpy as np
import matplotlib.pyplot as plt

#Definimos la función de activación para la Máquina de Hamming
def hamming_activation(input_pattern, weights):
    return np.dot(input_pattern, weights)

#Definimos la función de activación para la Red de Hopfield
def hopfield_activation(input_pattern, weights):
    return np.sign(np.dot(input_pattern, weights))

#Definimos la regla de aprendizaje de Hebb
def hebb_learning_rule(input_patterns):
    num_patterns, pattern_length = input_patterns.shape
    weights = np.zeros((pattern_length, pattern_length))
    for pattern in input_patterns:
        weights += np.outer(pattern, pattern)
    np.fill_diagonal(weights, 0)  #No hay conexiones de una neurona a sí misma
    return weights / num_patterns

#Definimos la regla de aprendizaje de Boltzmann
def boltzmann_learning_rule(input_patterns, learning_rate=0.1, epochs=100):
    num_patterns, pattern_length = input_patterns.shape
    weights = np.zeros((pattern_length, pattern_length))
    for _ in range(epochs):
        for pattern in input_patterns:
            activation = np.dot(pattern, weights)
            prob = 1 / (1 + np.exp(-activation))
            weights += learning_rate * (np.outer(pattern, pattern) - np.diag(pattern) @ weights)
    return weights

#Declaramos la Función para visualizar patrones y pesos
def visualize(input_patterns, weights, title):
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(input_patterns, cmap='binary')
    axs[0].set_title('Input Patterns')
    axs[0].set_xticks([])
    axs[0].set_yticks([])

    axs[1].imshow(weights, cmap='coolwarm', vmin=-1, vmax=1)
    axs[1].set_title('Weights')
    axs[1].set_xticks([])
    axs[1].set_yticks([])

    fig.suptitle(title)
    plt.show()

#Ejemplo de uso
input_patterns = np.array([[1, 1, 1, -1, -1],
                            [1, -1, 1, -1, 1]])

#Máquina de Hamming
weights_hamming = np.array([1, 1, 1, -1, -1])
result_hamming = hamming_activation(input_patterns, weights_hamming)
print("Resultado de la Máquina de Hamming:", result_hamming)

#Red de Hopfield
weights_hopfield = hebb_learning_rule(input_patterns)
result_hopfield = hopfield_activation(input_patterns[0], weights_hopfield)
print("Resultado de la Red de Hopfield:", result_hopfield)

#Regla de Aprendizaje de Hebb
print("Pesos aprendidos mediante la regla de Hebb:")
print(weights_hopfield)

#Regla de Aprendizaje de Boltzmann
weights_boltzmann = boltzmann_learning_rule(input_patterns)
print("Pesos aprendidos mediante la regla de Boltzmann:")
print(weights_boltzmann)

#Visualización de manera grafica para el usuario
visualize(input_patterns, weights_hopfield, "Red de Hopfield - Aprendizaje de Hebb")
visualize(input_patterns, weights_boltzmann, "Aprendizaje de Boltzmann")

