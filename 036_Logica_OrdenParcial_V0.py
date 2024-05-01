#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 36/59 Planificación de Orden Parcial

import matplotlib.pyplot as plt

# Definimos las tareas y sus dependencias
tareas = {
    'A': [],
    'B': ['A'],
    'C': ['A'],
    'D': ['B', 'C'],
    'E': ['D']
}

# Función para realizar la planificación de orden parcial
def planificacion_orden_parcial(tareas):
    plan = []  # Lista para almacenar el orden de ejecución de las tareas
    completado = set()  # Conjunto para mantener un registro de las tareas completadas

    # Mientras haya tareas por hacer
    while len(completado) < len(tareas):
        # Buscamos una tarea que pueda ser realizada
        for tarea, dependencias in tareas.items():
            if tarea not in completado and all(dep in completado for dep in dependencias):
                plan.append(tarea)  # Agregamos la tarea al plan
                completado.add(tarea)  # Marcamos la tarea como completada
                break

    return plan

# Ejecutamos la función de planificación
plan = planificacion_orden_parcial(tareas)

# Imprimimos el plan resultante
print("Plan de orden parcial:", plan)

# Visualización gráfica del plan
plt.figure(figsize=(8, 4))
plt.bar(range(len(plan)), [1] * len(plan), tick_label=plan)
plt.title('Planificación de Orden Parcial')
plt.xlabel('Tareas')
plt.ylabel('Tiempo')
plt.show()
