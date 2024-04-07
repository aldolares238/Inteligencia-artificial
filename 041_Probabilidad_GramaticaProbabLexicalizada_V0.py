#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 41/60 Gramáticas Probabilísticas Lexicalizadas

import nltk
from nltk.grammar import PCFG, induce_pcfg, Nonterminal
from nltk.corpus import treebank
import matplotlib.pyplot as plt

#Descargamos el corpus treebank de NLTK si no lo tenemos descargado
nltk.download('treebank')

#Obtenemos las producciones gramaticales a partir del corpus treebank
productions = []
for fileid in treebank.fileids():
    for tree in treebank.parsed_sents(fileid):
        productions += tree.productions()

#Creamos un símbolo no terminal para representar el símbolo inicial de la gramática
start_symbol = Nonterminal('S')

#Inducimos una gramática probabilística lexicalizada a partir de las producciones
grammar = induce_pcfg(start_symbol, productions)

#Imprimimos algunas estadísticas de la gramática
print("Número total de producciones:", len(grammar.productions()))
print("Número total de símbolos no terminales:", len(grammar._lhs_index.keys()))
print("Número total de símbolos terminales:", len(grammar._rhs_index.keys()))

#Graficamos la distribución de probabilidad de las producciones de la gramática
probabilities = [production.prob() for production in grammar.productions()]
plt.hist(probabilities, bins=20, edgecolor='black')
plt.title("Distribución de Probabilidad de las Producciones")
plt.xlabel("Probabilidad")
plt.ylabel("Frecuencia")
plt.show()
