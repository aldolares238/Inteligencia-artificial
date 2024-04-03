#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 22/60 Reconocimiento del Habla

import numpy as np
import matplotlib.pyplot as plt

#Definimos las posibles palabras que pueden ser reconocidas
palabras = ['hola', 'adios', 'gracias', 'por favor']

#Creamos un diccionario para almacenar las probabilidades de cada palabra
probabilidades = {'hola': 0.3, 'adios': 0.2, 'gracias': 0.25, 'por favor': 0.25}

#Función para mostrar la probabilidad de cada palabra en forma gráfica
def mostrar_probabilidades(probabilidades):
    plt.bar(range(len(probabilidades)), list(probabilidades.values()), align='center')
    plt.xticks(range(len(probabilidades)), list(probabilidades.keys()))
    plt.xlabel('Palabras')
    plt.ylabel('Probabilidad')
    plt.title('Probabilidades de las palabras')
    plt.show()

#Mostramos las probabilidades de las palabras
mostrar_probabilidades(probabilidades)

#Función para realizar el reconocimiento del habla
def reconocimiento_habla(probabilidades):
    #Obtenemos la palabra con la mayor probabilidad
    palabra_reconocida = max(probabilidades, key=probabilidades.get)
    #Devolvemos la palabra reconocida
    return palabra_reconocida

#Realizamos el reconocimiento del habla y mostramos el resultado
palabra_reconocida = reconocimiento_habla(probabilidades)
print("La palabra reconocida es:", palabra_reconocida)
