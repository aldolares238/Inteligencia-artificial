#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 21/60 Red Bayes. Dinámica: Filtrado de Partículas

import numpy as np
import matplotlib.pyplot as plt

#Dfinimos la función de movimiento de las partículas
def move_particles(particles, movement_variance):
    # Agregar ruido gaussiano al movimiento de las partículas
    noise = np.random.randn(particles.shape[0]) * movement_variance
    particles += noise
    return particles

#Deefinmos la función de observación (medición)
def observation_model(true_position, observation_variance):
    # Generar una observación con ruido gaussiano
    noise = np.random.randn() * observation_variance
    observation = true_position + noise
    return observation

#Definimos el algoritmo de filtrado de partículas (Red Bayes)
def particle_filter(initial_particles, num_particles, movement_variance, observation_variance, observations):
    particles = initial_particles
    
    #Creamos la Lista para almacenar las estimaciones de posición
    estimated_positions = []
    
    #Iteramos sobre las observaciones
    for observation in observations:
        #Movemos las partículas
        particles = move_particles(particles, movement_variance)
        
        #Clculamos la probabilidad de observación para cada partícula
        observation_probs = np.exp(-0.5 * ((particles - observation) / observation_variance)**2)
        
        #Normalizar las probabilidades
        observation_probs /= np.sum(observation_probs)
        
        #Estimamos la posición usando una ponderación por la probabilidad de observación
        estimated_position = np.sum(particles * observation_probs)
        estimated_positions.append(estimated_position)
        
        #Resamplear las partículas basadas en sus probabilidades de observación
        indices = np.random.choice(np.arange(num_particles), size=num_particles, p=observation_probs)
        particles = particles[indices]
    
    return estimated_positions

#Parámetros del problema
true_initial_position = 0  #posición inicial verdadera
movement_variance = 0.1   #Varianza del movimiento
observation_variance = 0.2  #Varianza de la observación
num_particles = 1000       #Número de partículas
num_observations = 50      #Número de observaciones

#Generar observaciones sintéticas
true_positions = [true_initial_position]
observations = []
for _ in range(num_observations):
    true_position = true_positions[-1] + np.random.randn() * movement_variance
    observation = observation_model(true_position, observation_variance)
    true_positions.append(true_position)
    observations.append(observation)

#Inicializar partículas
initial_particles = np.random.randn(num_particles) * movement_variance

#Ejecutar el filtro de partículas
estimated_positions = particle_filter(initial_particles, num_particles, movement_variance, observation_variance, observations)

#Visualización grafica para el usuario
plt.figure(figsize=(10, 6))
plt.plot(true_positions, label='Posición verdadera', color='blue')
plt.plot(observations, label='Observaciones', marker='o', linestyle='', color='red')
plt.plot(estimated_positions, label='Posición estimada', color='green', alpha=0.7)
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Filtrado de partículas con Red Bayes')
plt.legend()
plt.grid(True)
plt.show()
