#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 14/59 Programación Lógica: Prolog y CLIPS

import matplotlib.pyplot as plt
from pyDatalog import pyDatalog

# Definimos los hechos: en este caso, la relación entre algunos animales y sus características
pyDatalog.create_terms('es_gato, es_perro, es_pez, pelaje, tiene_alas')

+es_gato('Miau')
+pelaje('Miau', 'Pelo')
+es_perro('Rex')
+pelaje('Rex', 'Pelo')
+es_pez('Nemo')
+tiene_alas('Nemo', 'No') 

# Reglas lógicas: definimos las reglas que describen a un mamífero y a un animal con plumas
def es_mamifero(animal):
    return pelaje(animal, 'Pelo')  # Un animal es mamífero si tiene pelaje

def es_con_plumas(animal):
    return tiene_alas(animal, 'Si')  # Un animal tiene plumas si tiene alas

# Consultas lógicas: hacemos algunas consultas para demostrar el funcionamiento
print(es_mamifero('Miau'))  # ¿Es Miau un mamífero?
print(es_mamifero('Nemo'))  # ¿Es Nemo un mamífero?

print(es_con_plumas('Nemo'))  # ¿Tiene Nemo plumas?

# Crear un gráfico simple para mostrar los resultados
labels = ['Miau', 'Nemo']
mamifero = [1 if es_mamifero(animal) else 0 for animal in labels]
plumas = [1 if es_con_plumas(animal) else 0 for animal in labels]

x = range(len(labels))

plt.bar(x, mamifero, width=0.4, label='Mamífero')
plt.bar(x, plumas, width=0.4, label='Plumas', bottom=mamifero)

plt.xlabel('Animales')
plt.ylabel('Características')
plt.title('Animales y sus características')
plt.xticks(x, labels)
plt.legend()
plt.show()
