#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 45/60 Gráficos por Computador

import matplotlib.pyplot as plt  
#Definimos los resultados posibles al lanzar un dado
resultados = [1, 2, 3, 4, 5, 6]

#Definimos la probabilidad de cada resultado (en este caso, dado justo, así que cada resultado tiene la misma probabilidad)
probabilidades = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

#Creamos el gráfico de barras
plt.bar(resultados, probabilidades)

#Configuramos el título y etiquetas de los ejes
plt.title('Distribución de probabilidad al lanzar un dado')
plt.xlabel('Resultado')
plt.ylabel('Probabilidad')

#Mostramos el gráfico
plt.show()
