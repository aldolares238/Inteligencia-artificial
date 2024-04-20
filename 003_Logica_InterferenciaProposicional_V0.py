#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 3/59  Inferencia Lógica Proposicional

#Importamos la librería sympy para trabajar con lógica proposicional
import sympy as sp
import itertools
import matplotlib.pyplot as plt

#Creamos las variables proposicionales
p = sp.Symbol('p')
q = sp.Symbol('q')

#Definimos las expresiones lógicas utilizando las variables
expresion1 = p & q  # Conjunction (AND)
expresion2 = p | q  # Disjunction (OR)
expresion3 = ~p     # Negation (NOT)

#Generamos todas las combinaciones posibles de valores para p y q
combinaciones = list(itertools.product([True, False], repeat=2))

# Evaluamos las expresiones lógicas para cada combinación de valores
valores_expresion1 = [expresion1.subs({p: x[0], q: x[1]}) for x in combinaciones]
valores_expresion2 = [expresion2.subs({p: x[0], q: x[1]}) for x in combinaciones]
valores_expresion3 = [expresion3.subs({p: x[0], q: x[1]}) for x in combinaciones]

#Definimos una función para visualizar la tabla de verdad
def plot_truth_table(valores, title):
    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')
    ax.set_title(title)
    ax.table(cellText=[[str(x) for x in combinaciones[i]] + [str(valores[i])] for i in range(len(combinaciones))],
             colLabels=['p', 'q', 'Resultado'], loc='center')
    plt.show()

#Mostramos las tablas de verdad utilizando matplotlib
plot_truth_table(valores_expresion1, "Tabla de Verdad 1")
plot_truth_table(valores_expresion2, "Tabla de Verdad 2")
plot_truth_table(valores_expresion3, "Tabla de Verdad 3")

