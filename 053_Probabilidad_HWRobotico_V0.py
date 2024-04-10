#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 53/60 HW Robótico: Sensores y Actuadores

import numpy as np
import matplotlib.pyplot as plt

#Definimos la función para simular la probabilidad de un sensor
def sensor_probabilidad(estado_real):
    #Probabilidad de que el sensor reporte el estado real correctamente
    probabilidad_correcto = 0.8
    #Generamos un número aleatorio para simular la incertidumbre del sensor
    if np.random.rand() < probabilidad_correcto:
        #El sensor reporta el estado real con la probabilidad correcta
        return estado_real
    else:
        #El sensor reporta incorrectamente el estado real
        return not estado_real

#Definimos la función para simular la actuación del robot basado en los datos del sensor
def actuador(sensor):
    #Probabilidad de que el robot realice una acción basada en los datos del sensor
    probabilidad_accion = 0.7
    #Generamos un número aleatorio para simular la decisión del robot
    if np.random.rand() < probabilidad_accion:
        #El robot toma una acción basada en los datos del sensor
        return sensor
    else:
        #El robot toma una acción aleatoria
        return np.random.choice([True, False])

#Estado real del entorno
estado_real = True

#Simulamos la probabilidad del sensor
sensor = sensor_probabilidad(estado_real)

#Simulamos la actuación del robot basado en los datos del sensor
accion_robot = actuador(sensor)

#Visualizamos los resultados
print("Estado Real del Entorno:", estado_real)
print("Datos del Sensor:", sensor)
print("Acción del Robot:", accion_robot)

#Creamos un gráfico para visualizar los resultados
fig, ax = plt.subplots()

#Etiquetas para los estados
labels = ['Estado Real', 'Datos del Sensor', 'Acción del Robot']
# Valores para cada estado
values = [int(estado_real), int(sensor), int(accion_robot)]

#Creamos un gráfico de barras para visualizar los estados
ax.bar(labels, values)
ax.set_ylabel('Valor')
ax.set_title('Simulación de HW Robótico: Sensores y Actuadores')

#Mostramos el gráfico
plt.show()
