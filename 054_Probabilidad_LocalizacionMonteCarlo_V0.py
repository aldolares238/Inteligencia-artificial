#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 54/60 Localización: Monte-Carlo

import numpy as np
import matplotlib.pyplot as plt

#Definimos la función de localización Monte Carlo
def localizacion_monte_carlo(mapa, medidas, num_particulas, num_pasos):
    #Inicialización aleatoria de las partículas en el mapa
    particulas = np.random.randint(0, len(mapa), size=(num_particulas, 2))
    
    for _ in range(num_pasos):
        #Declaramos un Movimiento aleatorio de las partículas
        particulas[:, 0] += np.random.randint(-1, 2, size=num_particulas)
        particulas[:, 1] += np.random.randint(-1, 2, size=num_particulas)
        
        #Declaramos un Ajuste de las partículas dentro de los límites del mapa
        particulas[:, 0] = np.clip(particulas[:, 0], 0, len(mapa) - 1)
        particulas[:, 1] = np.clip(particulas[:, 1], 0, len(mapa[0]) - 1)
        
        #Calculamos la probabilidad de cada partícula dada la medida actual
        probabilidades = np.zeros(num_particulas)
        for i, (x, y) in enumerate(particulas):
            if mapa[x][y] == medidas:
                probabilidades[i] = 1
            else:
                probabilidades[i] = 0
                
        #Normalización de las probabilidades
        probabilidades /= np.sum(probabilidades)
        
        #Muestreo de partículas basado en las probabilidades
        particulas = particulas[np.random.choice(range(num_particulas), size=num_particulas, p=probabilidades)]
    
    return particulas

#Definimos un mapa para el ejemplo
mapa = np.array([[0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0],
                 [0, 1, 0, 0, 0]])

#Definición de las medidas
medidas = 1

#Parámetros del algoritmo
num_particulas = 1000
num_pasos = 10

#Ejecución del algoritmo
particulas_final = localizacion_monte_carlo(mapa, medidas, num_particulas, num_pasos)

#Visualización del resultado
plt.figure(figsize=(8, 8))
plt.imshow(mapa, cmap='gray', origin='lower')
plt.scatter(particulas_final[:, 1], particulas_final[:, 0], color='red', s=5)
plt.title('Localización Monte Carlo')
plt.xlabel('Columnas')
plt.ylabel('Filas')
plt.grid(True)
plt.show()
