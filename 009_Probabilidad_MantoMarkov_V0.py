#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 9/60 Manto de Markov
import random

#Definimos del corpus de texto de entrada
corpus = "el gato está en la casa y el perro también está en la casa"

#Funcion para dividir el texto en palabras
def tokenize_text(text):
    return text.split()

#Función para generar el modelo de Markov
def generate_markov_model(data):
    model = {}  #Inicializamos un diccionario para almacenar el modelo de Markov
    tokens = tokenize_text(data)  #Dividimos el texto en palabras
    for i in range(len(tokens) - 1):
        current_token = tokens[i]  #Guardamos Palabra actual
        next_token = tokens[i + 1]  #Siguiente palabra
        if current_token not in model:
            model[current_token] = {}  #Creamos una entrada para la palabra actual si no existe
        if next_token not in model[current_token]:
            model[current_token][next_token] = 0  #Inicializamos el conteo de transición si no existe
        model[current_token][next_token] += 1  #Incrementamos el conteo de la transición
    return model

#Generamos del modelo de Markov a partir del corpus
markov_model = generate_markov_model(corpus)

#Funcion para generar texto utilizando el modelo de Markov
def generate_text(model, length=10):
    generated_text = []  #Inicializamos una lista para almacenar el texto generado
    current_token = random.choice(list(model.keys()))  # Elige una palabra inicial aleatoria
    generated_text.append(current_token)  #Agregamos la palabra inicial al texto generado
    for _ in range(length):
        #Elegimos la siguiente palabra basada en las probabilidades de transición
        next_token = random.choices(
            list(model[current_token].keys()),
            weights=list(model[current_token].values())
        )[0]
        generated_text.append(next_token)  #Agregamos la siguiente palabra al texto generado
        current_token = next_token  #Actualizamos la palabra actual para la siguiente iteración
    return ' '.join(generated_text)  #Convertimos la lista de palabras en una cadena de texto

#Generamos de texto aleatorio utilizando el modelo de Markov
generated_text = generate_text(markov_model, length=15)
print("Texto generado usando el modelo de Markov:")
print(generated_text)  #Imprimimos el texto generado
