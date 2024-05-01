#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 39/59 Redes Jerárquicas de Tareas

import matplotlib.pyplot as plt

# Creamos un diccionario que representa las tareas y sus dependencias.
# Cada tarea es una clave y sus valores son las tareas que dependen de ella.
tareas = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

# Función para calcular la profundidad de una tarea en la jerarquía.
def calcular_profundidad(tarea):
    if tarea not in tareas or not tareas[tarea]:  # Si la tarea no tiene dependencias, su profundidad es 0.
        return 0
    else:
        # La profundidad de una tarea es uno más la profundidad máxima de sus dependencias.
        return 1 + max(calcular_profundidad(dependencia) for dependencia in tareas[tarea])

# Función para dibujar las tareas y sus dependencias.
def dibujar_red():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    # Posiciones de las tareas en el gráfico.
    posiciones = {}
    for nivel, tarea in enumerate(sorted(tareas.keys(), key=calcular_profundidad), start=1):
        posiciones[tarea] = (nivel, len(tareas[tarea]))

    # Dibujar las conexiones entre las tareas.
    for tarea, dependencias in tareas.items():
        for dependencia in dependencias:
            ax.plot([posiciones[tarea][0], posiciones[dependencia][0]],
                    [posiciones[tarea][1], posiciones[dependencia][1]], 'k-')

    # Dibujar las tareas.
    for tarea, posicion in posiciones.items():
        ax.text(posicion[0], posicion[1], tarea, ha='center', va='center')

    plt.show()

# Llamamos a la función para dibujar la red de tareas.
dibujar_red()
