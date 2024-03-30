#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 7/60 Red Bayesiana

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Definir la estructura de la red bayesiana
estructura_red = {
    'A': ['C'],
    'B': ['C']
}

# Definir las probabilidades condicionales
probabilidades = {
    'A': np.array([0.6, 0.4]),  # P(A)
    'B': np.array([0.7, 0.3]),  # P(B)
    'C': np.array([[[0.8, 0.9],  # P(C=0|A=0, B=0), P(C=1|A=0, B=0)
                    [0.6, 0.7]],  # P(C=0|A=0, B=1), P(C=1|A=0, B=1)
                   [[0.2, 0.1],  # P(C=0|A=1, B=0), P(C=1|A=1, B=0)
                    [0.4, 0.3]]]) # P(C=0|A=1, B=1), P(C=1|A=1, B=1)
}

# Definir una función para calcular la probabilidad condicional de C dadas las evidencias
def calcular_probabilidad_condicional(C, A, B):
    indice_a = A  # 0 si A=0, 1 si A=1
    indice_b = B  # 0 si B=0, 1 si B=1
    return probabilidades['C'][C, indice_a, indice_b]

# Realizar inferencia: calcular P(C=1|A=0, B=1)
probabilidad_condicional = calcular_probabilidad_condicional(1, 0, 1)
print("La probabilidad condicional de C=1 dado A=0, B=1 es:", probabilidad_condicional)

# Graficar la red bayesiana
G = nx.DiGraph(estructura_red)
nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=20, arrowsize=20)
plt.show()


