#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 40/59 Planificación Condicional

import matplotlib.pyplot as plt

# Definimos las acciones posibles
acciones = {
    'despertarse': {'costo': 1, 'precondiciones': []},
    'levantarse': {'costo': 1, 'precondiciones': ['despertarse']},
    'tomar_cafe': {'costo': 2, 'precondiciones': ['levantarse']},
    'ir_a_trabajo': {'costo': 2, 'precondiciones': ['despertarse', 'levantarse', 'tomar_cafe']},
    'trabajar': {'costo': 3, 'precondiciones': ['ir_a_trabajo']}
}

# Definimos el estado inicial y el objetivo
estado_inicial = ['despertarse']
objetivo = ['trabajar']

# Función para verificar si un estado satisface una condición
def satisfacer_condicion(estado, condicion):
    return condicion in estado

# Función para aplicar una acción y obtener el nuevo estado
def aplicar_accion(estado, accion):
    for precondicion in acciones[accion]['precondiciones']:
        if not satisfacer_condicion(estado, precondicion):
            return None  # No se puede aplicar la acción
    nuevo_estado = estado.copy()
    nuevo_estado.append(accion)
    return nuevo_estado

# Función para buscar una planificación utilizando búsqueda en profundidad
def planificacion_condicional(estado_actual, objetivo, acciones_disponibles, max_profundidad, plan_actual=[]):
    if estado_actual == objetivo:
        return plan_actual
    if max_profundidad == 0:
        return None
    for accion in acciones_disponibles:
        nuevo_estado = aplicar_accion(estado_actual, accion)
        if nuevo_estado is not None:
            nuevo_plan = plan_actual + [accion]
            resultado = planificacion_condicional(nuevo_estado, objetivo, acciones_disponibles, max_profundidad - 1, nuevo_plan)
            if resultado is not None:
                return resultado
    return None

# Definimos una profundidad máxima de búsqueda
profundidad_maxima = 10

# Encontrar el plan
plan = planificacion_condicional(estado_inicial, objetivo, acciones.keys(), profundidad_maxima)

# Imprimir el plan
if plan is not None:
    print("Plan encontrado:", plan)
    
    # Visualización gráfica
    plt.figure(figsize=(8, 6))
    plt.plot(range(len(plan)), [acciones[accion]['costo'] for accion in plan], marker='o')
    plt.xlabel('Paso')
    plt.ylabel('Costo')
    plt.title('Costo de cada acción en el plan')
    plt.xticks(range(len(plan)), plan)
    plt.grid(True)
    plt.show()
else:
    print("No se encontró un plan.")

