#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 2/60 Probabilidad a Priori

import matplotlib.pyplot as plt

#Definimos las categorías o clases posibles
categorias = ['A', 'B', 'C']

#Definimos las probabilidades a priori de cada categoría
probabilidades_priori = {'A': 0.3, 'B': 0.5, 'C': 0.2}

#Calculamos el total de las probabilidades a priori
total_probabilidades_priori = sum(probabilidades_priori.values())

#Normalizamos las probabilidades a priori para asegurarnos de que sumen 1
for categoria in categorias:
    probabilidades_priori[categoria] /= total_probabilidades_priori

#Mostramos las probabilidades a priori normalizadas
print("Probabilidades a priori normalizadas:")
for categoria in categorias:
    print(f"Probabilidad a priori de {categoria}: {probabilidades_priori[categoria]}")

#Creamos un gráfico de barras para visualizar las probabilidades a priori
plt.bar(categorias, probabilidades_priori.values())
plt.title('Probabilidades a Priori')
plt.xlabel('Categorías')
plt.ylabel('Probabilidades')
plt.show()
