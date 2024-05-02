#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 53/59 Gramáticas: Jerarquía de Chomsky

import matplotlib.pyplot as plt

# Definimos los tipos de gramáticas de la jerarquía de Chomsky
tipos_gramaticas = ['Tipo 0', 'Tipo 1', 'Tipo 2', 'Tipo 3']

# Definimos las propiedades de cada tipo de gramática
propiedades = {
    'Tipo 0': 'Gramáticas recursivas generales',
    'Tipo 1': 'Gramáticas sensibles al contexto',
    'Tipo 2': 'Gramáticas libres de contexto',
    'Tipo 3': 'Gramáticas regulares'
}

# Definimos la complejidad de cada tipo de gramática
complejidad = {
    'Tipo 0': 4,
    'Tipo 1': 3,
    'Tipo 2': 2,
    'Tipo 3': 1
}

# Visualizamos las propiedades de cada tipo de gramática
plt.bar(tipos_gramaticas, [complejidad[tipo] for tipo in tipos_gramaticas], color='skyblue')
plt.xlabel('Tipo de Gramática')
plt.ylabel('Complejidad')
plt.title('Jerarquía de Chomsky: Tipos de Gramáticas')
plt.ylim(0, 5)

# Añadimos etiquetas con las propiedades de cada tipo de gramática
for i, tipo in enumerate(tipos_gramaticas):
    plt.text(i, complejidad[tipo] + 0.1, propiedades[tipo], ha='center')

plt.show()
