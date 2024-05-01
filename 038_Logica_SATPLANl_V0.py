#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 38/59 Planificación Lógica Proposicional: SATPLAN

from pysat.solvers import Glucose3
import matplotlib.pyplot as plt

# Definición del problema en forma de cláusulas
# Cada cláusula es una lista de literales. Un literal es una variable o su negación.
clauses = [[1, 2], [-1, 3], [-2, -3], [-1, -2], [3]]

# Crear un solucionador SAT
solver = Glucose3()

# Agregar cláusulas al solucionador
for clause in clauses:
    solver.add_clause(clause)

# Resolver el problema SAT
if solver.solve():
    # Si hay una solución, obtener los valores de verdad de las variables
    model = solver.get_model()
    print("Solución encontrada:")
    print(model)
    
    # Visualización gráfica de la solución
    plt.figure(figsize=(5, 5))
    for var in range(1, 4):
        # Convertir el valor de verdad de la variable en un color para visualización
        color = 'green' if model[var-1] > 0 else 'red'
        plt.scatter(var, 0, color=color, s=100)
        plt.text(var, 0.1, f'x{var}={model[var-1]}', horizontalalignment='center')
    plt.title("Visualización de la solución")
    plt.xticks([1, 2, 3], ['x1', 'x2', 'x3'])
    plt.yticks([])
    plt.xlim(0.5, 3.5)
    plt.ylim(-0.5, 0.5)
    plt.show()
    
else:
    print("No se encontró solución para el problema SAT.")
