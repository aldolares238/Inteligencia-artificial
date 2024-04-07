#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 44/60 Traducción Automática Estadística

import numpy as np
import matplotlib.pyplot as plt

#Definimos las palabras en el idioma de origen (ingles) y en el idioma objetivo (español)
source_words = ['I', 'like', 'cats']
target_words = ['Me', 'gustan', 'los', 'gatos']

#Inicializamos la tabla de probabilidades de alineación con valores aleatorios
alignment_probs = np.random.rand(len(source_words), len(target_words))

#Normalizamos las probabilidades para que sumen 1 en cada fila
alignment_probs /= np.sum(alignment_probs, axis=1, keepdims=True)

#Visualizamos la matriz de probabilidades de alineación
plt.imshow(alignment_probs, cmap='hot', interpolation='nearest')
plt.title('Matriz de Probabilidades de Alineación')
plt.xlabel('Palabras en español')
plt.ylabel('Palabras en inglés')
plt.xticks(np.arange(len(target_words)), target_words)
plt.yticks(np.arange(len(source_words)), source_words)
plt.colorbar()
plt.show()
