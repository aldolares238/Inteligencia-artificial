#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 8/59 Algoritmos de Búsqueda Local

import numpy as np
import matplotlib.pyplot as plt

#Definimos la función objetivo, en este caso una función cuadrática
def objective_function(x):
    return x**2

#Definimos el rango de valores para x
x_values = np.linspace(-5, 5, 100)

#Calculamos los valores de la función objetivo para cada valor de x
y_values = objective_function(x_values)

#Inicializamos la solución inicial aleatoriamente
current_solution = np.random.uniform(-5, 5)

#Establecemos el número máximo de iteraciones
max_iterations = 100

#Inicializamos una lista para almacenar el historial de soluciones
solution_history = [current_solution]

#Iteramos el algoritmo de búsqueda local
for i in range(max_iterations):
    #Evaluamos la función objetivo en la solución actual
    current_cost = objective_function(current_solution)
    
    #Generamos una nueva solución vecina ligeramente modificando la solución actual
    #Aquí podrías implementar diferentes estrategias de búsqueda local, como por ejemplo, perturbación aleatoria
    new_solution = current_solution + np.random.uniform(-0.5, 0.5)
    
    #Calculamos el costo de la nueva solución
    new_cost = objective_function(new_solution)
    
    #Si la nueva solución es mejor que la actual, la aceptamos como la nueva solución actual
    if new_cost < current_cost:
        current_solution = new_solution
        solution_history.append(current_solution)

# Mostramos el proceso de búsqueda local gráficamente
plt.plot(x_values, y_values, label='Función Objetivo')
plt.scatter(solution_history, [objective_function(sol) for sol in solution_history], color='red', label='Soluciones Evaluadas')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Algoritmo de Búsqueda Local')
plt.legend()
plt.grid(True)
plt.show()

# Mostramos la solución final
print("Solución final encontrada:", current_solution)
print("Valor de la función objetivo en la solución final:", objective_function(current_solution))
