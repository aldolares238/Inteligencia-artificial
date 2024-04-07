#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 37/60 Mapas Autoorganizados de Kohonen


import numpy as np
import matplotlib.pyplot as plt

#Definimod la Función para inicializar los pesos aleatoriamente
def initialize_weights(input_dim, output_dim):
    return np.random.rand(output_dim, input_dim)

#Definimos la Función para calcular la distancia euclidiana entre dos vectores
def euclidean_distance(a, b):
    return np.linalg.norm(a - b)

#Definimos la Función para encontrar la neurona ganadora
def find_winner(input_vector, weights):
    distances = [euclidean_distance(input_vector, weight) for weight in weights]
    return np.argmin(distances)

#Definimos la Función para actualizar los pesos de los vecinos de la neurona ganadora
def update_weights(input_vector, winner, weights, learning_rate, neighborhood_radius):
    for i, weight in enumerate(weights):
        distance_to_winner = np.abs(i - winner)
        if distance_to_winner <= neighborhood_radius:
            #Calculamos el factor de influencia del vecino
            influence = learning_rate * np.exp(-distance_to_winner / (2 * neighborhood_radius))
            #Actualizamos el peso del vecino
            weights[i] += influence * (input_vector - weight)

#Declaramos los Datos de entrada (aleatorios para este ejemplo)
data = np.random.rand(100, 2)

#Declaramos los Parámetros del mapa autoorganizado
input_dim = data.shape[1]
output_dim = 10  # Dimensión del mapa, puedes ajustarlo según el problema
epochs = 100  # Número de iteraciones
learning_rate = 0.1  # Tasa de aprendizaje
initial_neighborhood_radius = output_dim / 2  # Radio inicial del vecindario

#Inicializamos los pesos
weights = initialize_weights(input_dim, output_dim)

#Entrenamiento del mapa
for epoch in range(epochs):
    np.random.shuffle(data)  #Barajar los datos en cada época
    for input_vector in data:
        #Encontrar la neurona ganadora
        winner = find_winner(input_vector, weights)
        #Vtualizar los pesos de los vecinos de la neurona ganadora
        update_weights(input_vector, winner, weights, learning_rate, initial_neighborhood_radius)

#Visualización de manera grafica para el usuario
plt.scatter(data[:, 0], data[:, 1], color='b', label='Datos de entrada')
plt.scatter(weights[:, 0], weights[:, 1], color='r', marker='x', label='Neuronas')
plt.title('Mapa Autoorganizado de Kohonen')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
