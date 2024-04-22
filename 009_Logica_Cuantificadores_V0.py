#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 9/59 Sintaxis y Semántica: Cuantificadores

import matplotlib.pyplot as plt

# Definimos una función para evaluar un predicado sobre un conjunto
def evaluate_predicate(predicate, domain):
    #Función que evalúa un predicado sobre un conjunto.

    return [predicate(x) for x in domain]

# Definimos el dominio de nuestra función
domain = list(range(-10, 11))

# Definimos el predicado "es_par"
def es_par(x):
    #Función que verifica si un número es par.

    return x % 2 == 0

# Evaluamos el predicado "es_par" en nuestro dominio
valores_es_par = evaluate_predicate(es_par, domain)

# Creamos un gráfico para visualizar los resultados
plt.plot(domain, valores_es_par, label='es_par(x)')
plt.xlabel('x')
plt.ylabel('es_par(x)')
plt.title('Predicado: es_par(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()
