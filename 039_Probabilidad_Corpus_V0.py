#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 39/60 Modelo Probabilístico del Lenguaje: Corpus

import numpy as np
import matplotlib.pyplot as plt

#Definimos una pequeña muestra de texto como corpus
corpus = "el alumno hace tarea el maestro deja tarea la tarea es aburrida el almnno es infeliz"

#Convertimos el texto a minúsculas y dividimos las palabras en una lista
corpus = corpus.lower().split()

#Creamos un diccionario para almacenar las frecuencias de cada palabra
frecuencias = {}

# ontamos la frecuencia de cada palabra en el corpus
for palabra in corpus:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

#Calculamos las probabilidades de cada palabra
total_palabras = len(corpus)
probabilidades = {palabra: frecuencia / total_palabras for palabra, frecuencia in frecuencias.items()}

#Mostramos las probabilidades de cada palabra
print("Probabilidades de cada palabra:")
for palabra, probabilidad in probabilidades.items():
    print(f"{palabra}: {probabilidad:.2f}")

#Visualizamos las probabilidades en un gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(probabilidades.keys(), probabilidades.values(), color='skyblue')
plt.xlabel('Palabra')
plt.ylabel('Probabilidad')
plt.title('Probabilidades de cada palabra en el corpus')
plt.xticks(rotation=45)
plt.show()
