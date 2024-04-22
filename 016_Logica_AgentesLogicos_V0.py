#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 16/59 Agentes Lógicos

import matplotlib.pyplot as plt

# Función para evaluar la proposición lógica
def evaluate_proposition(A, B, C):
    return (A and B) or (not B and C)

# Valores para las variables lógicas
A_values = [True, True, False, False]
B_values = [True, False, True, False]
C_values = [True, False, False, True]

# Resultados de la evaluación de la proposición lógica para cada combinación de valores
results = [evaluate_proposition(A, B, C) for A, B, C in zip(A_values, B_values, C_values)]

# Gráfico de barras para mostrar los resultados
plt.bar(range(len(results)), results, color=['green' if res else 'red' for res in results])
plt.title('Resultados de la evaluación de la proposición lógica')
plt.xlabel('Combinación de valores')
plt.ylabel('Resultado (True/False)')
plt.xticks(range(len(results)), [f'({A}, {B}, {C})' for A, B, C in zip(A_values, B_values, C_values)])
plt.yticks([0, 1], ['False', 'True'])
plt.show()
