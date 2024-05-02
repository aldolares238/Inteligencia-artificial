#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 41/59 Vigilancia de Ejecución y Replanificación

import matplotlib.pyplot as plt
import numpy as np
import time

# Definición de las tareas y sus tiempos de ejecución estimados
tareas = {
    "Tarea A": 4,
    "Tarea B": 3,
    "Tarea C": 2,
    "Tarea D": 5
}

# Tiempo límite para completar todas las tareas
tiempo_limite = 10

# Función para simular la ejecución de una tarea
def ejecutar_tarea(nombre, tiempo):
    print(f"Ejecutando {nombre}...")
    time.sleep(tiempo)
    print(f"{nombre} completada.")

# Función para mostrar el progreso de las tareas
def mostrar_progreso(tareas_completadas):
    plt.bar(range(len(tareas)), tareas_completadas.values(), align='center')
    plt.xticks(range(len(tareas)), list(tareas_completadas.keys()))
    plt.xlabel('Tareas')
    plt.ylabel('Tiempo (s)')
    plt.title('Progreso de las tareas')
    plt.show()

# Inicialización del progreso de las tareas
tareas_completadas = {tarea: 0 for tarea in tareas}

# Ejecución de las tareas
for tarea, tiempo in tareas.items():
    ejecutar_tarea(tarea, tiempo)
    tareas_completadas[tarea] = tiempo

    # Verificar si se supera el tiempo límite
    tiempo_transcurrido = sum(tareas_completadas.values())
    if tiempo_transcurrido > tiempo_limite:
        print("¡Se ha superado el tiempo límite!")
        break

    mostrar_progreso(tareas_completadas)
