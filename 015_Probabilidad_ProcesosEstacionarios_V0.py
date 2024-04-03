#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 15/60 Procesos Estacionarios


import numpy as np
import matplotlib.pyplot as plt

#Definimos una función que simula el proceso estacionario
def proceso_estacionario(n_steps=1000): #Asignamos el parametro necesario
    # Creamos un array para almacenar los valores del proceso general
    proceso = np.zeros(n_steps)
    
    #Definimos las probabilidades de los posibles estados durante el proceso
    probabilidades = [0.4, 0.3, 0.2, 0.1]
    
    #Definimos los posibles estados
    estados = [-3, -1, 1, 3]
    
    #Escogemos un estado inicial al azar
    proceso[0] = np.random.choice(estados)
    
    #Simulamos el proceso
    for t in range(1, n_steps):
        #Calculamos el siguiente estado basado en el estado actual
        proceso[t] = np.random.choice(estados, p=probabilidades)
    
    return proceso

#Simulamos el proceso estacionario
proceso = proceso_estacionario()

#Mostramos el proceso en un gráfico añadiendo colores y etiquetas
plt.figure(figsize=(10, 6))
plt.plot(proceso, color='blue', alpha=0.7, linewidth=1.5)
plt.title('Proceso Estacionario')
plt.xlabel('Tiempo')
plt.ylabel('Estado')
plt.grid(True)
plt.show()
