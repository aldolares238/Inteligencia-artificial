#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 1/60 Incertidumbre

import numpy as np
import matplotlib.pyplot as plt

#Definimos la función de incertidumbre que calcula la probabilidad de obtener caras
def incertidumbre(num_lanzamientos, num_caras): #La funcion recibe como parametro el numero de lanzamientos y caras
    return num_caras / num_lanzamientos

#Número de lanzamientos de la moneda
num_lanzamientos = 100

#Simulamos lanzar la moneda
lanzamientos = np.random.choice(['cara', 'cruz'], num_lanzamientos)

#Contamos el número de caras
num_caras = np.sum(lanzamientos == 'cara')

#Calculamos la incertidumbre
probabilidad_caras = incertidumbre(num_lanzamientos, num_caras)

#Graficamos los resultados
etiquetas = ['Caras', 'Cruces']
valores = [num_caras, num_lanzamientos - num_caras]
colores = ['blue', 'red']

plt.pie(valores, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Resultado de lanzamientos de moneda')
plt.show()

#Imprimimos la probabilidad de obtener caras al usuario
print("La probabilidad de obtener caras es:", probabilidad_caras)

