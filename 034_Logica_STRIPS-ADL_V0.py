#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 34/59 Algoritmos de Planificación: STRIPS y ADL

import matplotlib.pyplot as plt

# Definimos las acciones disponibles en nuestro dominio
actions = {
    'move(a, b)': {'pre': {'at(a)'}, 'add': {'at(b)'}, 'delete': {'at(a)'}},
    'move(b, c)': {'pre': {'at(b)'}, 'add': {'at(c)'}, 'delete': {'at(b)'}}
}

# Estado inicial
initial_state = {'at(a)'}

# Estado objetivo
goal_state = {'at(c)'}

# Implementación del algoritmo STRIPS
def strips(initial_state, goal_state, actions):
    plan = []
    state = initial_state.copy()
    while state != goal_state:
        applicable_actions = [action for action in actions.keys() if actions[action]['pre'].issubset(state)]
        if not applicable_actions:
            raise Exception("No plan found!")
        for action in applicable_actions:
            state.difference_update(actions[action]['delete'])
            state.update(actions[action]['add'])
            plan.append(action)
    return plan

# Ejecutamos el algoritmo STRIPS
plan = strips(initial_state, goal_state, actions)
print("Plan generado por STRIPS:", plan)

# Graficamos el plan generado
plt.figure(figsize=(8, 4))
plt.plot(range(len(plan)), [0] * len(plan), 'bo-', markersize=12)  # Representamos las acciones en el plan
plt.yticks([], [])
plt.xticks(range(len(plan)), plan)  # Etiquetamos las acciones en el eje x
plt.title("Plan generado por STRIPS")
plt.xlabel("Paso")
plt.ylabel("Acción")
plt.grid(True)
plt.show()
