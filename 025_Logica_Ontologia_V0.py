#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 25/59 Ingeniería del Conocimiento: Ontologías

import matplotlib.pyplot as plt

# Creamos un diccionario que representará nuestra ontología
# Cada animal será una clave y sus características serán los valores asociados
ontologia = {
    'Perro': ['Cuadrúpedo', 'Doméstico'],
    'Gato': ['Cuadrúpedo', 'Doméstico'],
    'Pájaro': ['Bípedo', 'Doméstico'],
    'Serpiente': ['Sin patas', 'Salvaje']
}

# Extraemos las características únicas para cada animal
# Esto nos ayudará a etiquetar los ejes del gráfico
caracteristicas = set()
for animal, caracteristicas_animal in ontologia.items():
    caracteristicas.update(caracteristicas_animal)

# Creamos listas para los ejes x e y del gráfico
x = list(caracteristicas)
y = list(ontologia.keys())

# Creamos una matriz de valores booleanos para indicar si un animal tiene una característica
valores = []
for animal in y:
    fila = []
    for caracteristica in x:
        if caracteristica in ontologia[animal]:
            fila.append(1)
        else:
            fila.append(0)
    valores.append(fila)

# Creamos el gráfico
plt.figure(figsize=(8, 6))
plt.imshow(valores, cmap='binary', aspect='auto', interpolation='nearest')

# Añadimos etiquetas a los ejes
plt.xticks(range(len(x)), x)
plt.yticks(range(len(y)), y)
plt.xlabel('Características')
plt.ylabel('Animales')

# Añadimos una barra de color para representar la presencia o ausencia de una característica
plt.colorbar(label='Presencia')

# Mostramos el gráfico
plt.title('Ontología Animal')
plt.show()
