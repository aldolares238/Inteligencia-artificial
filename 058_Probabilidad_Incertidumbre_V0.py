#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 58/60 Incertidumbre

import random
import matplotlib.pyplot as plt

#Definimos la función para simular el lanzamiento del dado
def lanzar_dado():
    return random.randint(1, 6)  # Genera un número aleatorio entre 1 y 6

#Definimos el número de veces que vamos a lanzar el dado
num_lanzamientos = 1000

#Inicializamos la lista para almacenar los resultados de los lanzamientos
resultados = []

#Lanzamos el dado y almacenamos los resultados
for _ in range(num_lanzamientos):
    resultados.append(lanzar_dado())

#Contamos cuántas veces salió un número par
num_pares = sum(1 for resultado in resultados if resultado % 2 == 0)

#Calculamos la probabilidad de que salga un número par
probabilidad_par = num_pares / num_lanzamientos

#Creamos un gráfico de barras para visualizar los resultados
etiquetas = ['Pares', 'Impares']
valores = [num_pares, num_lanzamientos - num_pares]
plt.bar(etiquetas, valores, color=['blue', 'red'])
plt.title('Resultados de lanzar un dado')
plt.xlabel('Resultado')
plt.ylabel('Frecuencia')
plt.show()

#Imprimimos la probabilidad de que salga un número par
print("La probabilidad de que salga un número par es: {:.2f}".format(probabilidad_par))
