#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 32/59  Sistemas expertos

import matplotlib.pyplot as plt

# Definimos las características de las frutas: peso y textura (0: rugosa, 1: lisa)
frutas = {'manzana': [[150, 0], [130, 0], [160, 1], [140, 1]], 
          'naranja': [[150, 1], [130, 1], [160, 0], [140, 0]]}

# Visualizamos las características de las frutas
for fruta, caracteristicas in frutas.items():
    peso = [caracteristica[0] for caracteristica in caracteristicas]
    textura = [caracteristica[1] for caracteristica in caracteristicas]
    if fruta == 'manzana':
        plt.scatter(peso, textura, color='red', label='Manzana')
    else:
        plt.scatter(peso, textura, color='orange', label='Naranja')

# Definimos la fruta desconocida
fruta_desconocida = [145, 0]  # peso: 145g, textura: rugosa

# Visualizamos la fruta desconocida
plt.scatter(fruta_desconocida[0], fruta_desconocida[1], color='green', label='Fruta Desconocida')

# Etiquetamos los ejes
plt.xlabel('Peso (g)')
plt.ylabel('Textura (0: Rugosa, 1: Lisa)')

# Mostramos la leyenda
plt.legend()

# Mostramos el gráfico
plt.title('Clasificación de Frutas')
plt.grid(True)
plt.show()

# Definimos la función para determinar la fruta
def sistema_experto(fruta):
    if fruta[0] > 140 and fruta[1] == 1:
        return "Es una manzana"
    elif fruta[0] < 140 and fruta[1] == 0:
        return "Es una naranja"
    else:
        return "No se puede determinar"

# Aplicamos el sistema experto a la fruta desconocida
resultado = sistema_experto(fruta_desconocida)
print("El resultado es:", resultado)
