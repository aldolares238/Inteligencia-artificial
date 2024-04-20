#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 5/59 Resolución y Forma Normal Conjuntiva

import matplotlib.pyplot as plt
import networkx as nx

#Función para convertir la expresión lógica en un grafo dirigido
def expresion_a_grafo(expresion):
    G = nx.DiGraph()
    nodos = list(expresion.atoms())
    for nodo in nodos:
        G.add_node(nodo)
    clausulas = expresion.args
    for clausula in clausulas:
        if isinstance(clausula, Or):
            for literal in clausula.args:
                if isinstance(literal, Not):
                    G.add_edge(literal.args[0], clausula)
                else:
                    G.add_edge(literal, clausula)
        elif isinstance(clausula, And):
            for literal in clausula.args:
                if isinstance(literal, Not):
                    G.add_edge(clausula, literal.args[0])
    return G

#Función para dibujar el grafo
def dibujar_grafo(G):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=15, font_weight="bold")
    plt.title("Expresión Lógica como Grafo")
    plt.show()

#Importamos la librería para manipulación simbólica
from sympy import symbols, And, Or, Not, to_cnf

#Definimos los símbolos
A, B, C = symbols('A B C')

#Definimos la expresión en forma de cláusulas
expresion = Or(And(A, B), And(Not(A), C), Or(Not(B), C))

#Convertimos la expresión a CNF
cnf_expresion = to_cnf(expresion)

#Mostramos la expresión en CNF
print("Expresión en CNF:", cnf_expresion)

#Convertimos la expresión lógica en un grafo dirigido
grafo = expresion_a_grafo(cnf_expresion)

#Dibujamos el grafo
dibujar_grafo(grafo)
