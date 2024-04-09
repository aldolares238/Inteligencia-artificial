#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 49/60 Reconocimiento de Objetos

import numpy as np
import matplotlib.pyplot as plt

#Definimos las probabilidades iniciales de que un objeto sea de cierto tipo
probabilidades = {'perro': 0.3, 'gato': 0.2, 'pajaro': 0.5}

#Creamos una lista con los tipos de objetos
objetos = list(probabilidades.keys())

#Creamos un array con las probabilidades
prob_array = np.array(list(probabilidades.values()))

#Declaramos la Función para simular la observación de un objeto
def observar_objeto():
    #Generamos un número aleatorio entre 0 y 1
    rnd = np.random.rand()
    #Inicializamos la suma acumulada de probabilidades
    acumulado = 0
    #Iteramos sobre los objetos y sus probabilidades
    for i in range(len(prob_array)):
        #Sumamos la probabilidad del objeto actual al acumulado
        acumulado += prob_array[i]
        #Si el número aleatorio está dentro del rango de esta probabilidad
        if rnd < acumulado:
            #Retornamos el objeto correspondiente
            return objetos[i]

#Simulamos la observación de un objeto
objeto_observado = observar_objeto()

#Imprimimos el objeto observado
print("Se observó un:", objeto_observado)

#Creamos un gráfico de barras para visualizar las probabilidades
plt.bar(objetos, prob_array)
plt.title('Probabilidades de cada objeto')
plt.xlabel('Objeto')
plt.ylabel('Probabilidad')
plt.show()
