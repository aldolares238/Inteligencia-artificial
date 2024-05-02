#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 55/59 Análisis Sintáctico

import matplotlib.pyplot as plt

# Definimos una gramática de ejemplo en formato CFG
gramatica = """
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'boy' | 'girl' | 'dog' | 'cat'
    V -> 'saw' | 'chased' | 'bit' | 'ate'
    P -> 'with' | 'in'
"""

# Definimos una frase de ejemplo para analizar sintácticamente
frase = "the boy saw a dog with a cat"

# Tokenizamos la frase utilizando el método split()
palabras = frase.split()

# Visualizamos las palabras tokenizadas
print("Palabras tokenizadas:", palabras)

# Visualizamos la frase tokenizada
plt.figure(figsize=(8, 6))
plt.text(0.5, 0.5, frase, fontsize=14, ha='center')
plt.axis('off')
plt.title('Frase Original')
plt.show()
