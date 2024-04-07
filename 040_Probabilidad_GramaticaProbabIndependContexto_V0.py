#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 40/60 Gramáticas Probab. Independ. del Contexto

import random

#Definimos la gramática probabilística
grammar = {
    'S': [('NP', 'VP')],
    'NP': [('Det', 'Noun')],
    'VP': [('Verb', 'NP')],
    'Det': ['the', 'a'],
    'Noun': ['cat', 'dog', 'man', 'woman'],
    'Verb': ['runs', 'jumps', 'eats']
}

#Declaramos la Función para generar una oración aleatoria basada en la gramática
def generate_sentence(grammar, start_symbol):
    if start_symbol not in grammar:
        return start_symbol
    
    #Selecciona una de las reglas de producción basada en la probabilidad
    expansion = random.choices(grammar[start_symbol])[0]
    
    #Expande recursivamente las reglas de producción
    return ' '.join(generate_sentence(grammar, symbol) for symbol in expansion)

#Genera una oración aleatoria
random_sentence = generate_sentence(grammar, 'S')
print("Oración generada:", random_sentence)
