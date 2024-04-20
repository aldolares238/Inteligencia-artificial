#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 4/59 - Equivalencia, Validez y Satisfacibilidad

import sympy as sp
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

#Creamos las variables simbólicas
p, q = sp.symbols('p q')

# Definimos dos expresiones lógicas
exp1 = p & q  # Conjunction (AND)
exp2 = p | q  # Disjunction (OR)

#Imprimimos las expresiones
print("Expresión 1:", exp1)
print("Expresión 2:", exp2)

#Comprobamos la equivalencia entre las expresiones
equivalencia = exp1.equals(exp2)  # Verifica si las expresiones son equivalentes
print("¿Las expresiones son equivalentes?", equivalencia)

#Comprobamos si las expresiones son válidas
validacion1 = sp.satisfiable(exp1)  # Verifica si la expresión 1 es satisfacible
validacion2 = sp.satisfiable(exp2)  # Verifica si la expresión 2 es satisfacible
print("¿La expresión 1 es válida?", validacion1)
print("¿La expresión 2 es válida?", validacion2)

#Creamos un diccionario para asignar valores de verdad a las variables
valores = {p: True, q: False}

#Evaluamos las expresiones con los valores de verdad dados
evaluacion1 = exp1.subs(valores)  # Evaluamos la expresión 1
evaluacion2 = exp2.subs(valores)  # Evaluamos la expresión 2
print("Evaluación de la expresión 1 con p=True, q=False:", evaluacion1)
print("Evaluación de la expresión 2 con p=True, q=False:", evaluacion2)

#Creamos un diagrama de Venn para representar las expresiones
venn_labels = ('p', 'q', 'p & q')
venn_sets = {'10': 1, '01': 1, '11': 1}

#Creamos la figura y los subplots
fig, axes = plt.subplots(1, 2)

#Dibujamos los diagramas de Venn para cada expresión
venn2(subsets=venn_sets, set_labels=venn_labels, ax=axes[0])
venn2(subsets=venn_sets, set_labels=venn_labels, ax=axes[1])

#Agregamos títulos para cada subgráfico
axes[0].set_title('Expresión 1: p & q')
axes[1].set_title('Expresión 2: p | q')

#Mostramos los gráficos
plt.show()
