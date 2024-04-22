#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 22/59 Lógica Difusa: Conjuntos Difusos

import numpy as np
import matplotlib.pyplot as plt

# Función de pertenencia triangular
def triangular(x, a, b, c):
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))

# Definir universo y conjuntos difusos para la variable "edad"
edad = np.arange(0, 101, 1)
joven = triangular(edad, 0, 0, 50)
viejo = triangular(edad, 50, 100, 100)

# Visualización de las funciones de membresía para la variable "edad"
plt.figure()
plt.plot(edad, joven, label='Joven')
plt.plot(edad, viejo, label='Viejo')
plt.title('Conjuntos difusos para la variable "edad"')
plt.xlabel('Edad')
plt.ylabel('Membresía')
plt.legend()
plt.grid()
plt.show()

# Definir universo y conjuntos difusos para la variable de salida "salida"
salida = np.arange(0, 101, 1)
bajo = triangular(salida, 0, 0, 50)
alto = triangular(salida, 50, 100, 100)

# Visualización de las funciones de membresía para la variable de salida "salida"
plt.figure()
plt.plot(salida, bajo, label='Bajo')
plt.plot(salida, alto, label='Alto')
plt.title('Conjuntos difusos para la variable de salida "salida"')
plt.xlabel('Salida')
plt.ylabel('Membresía')
plt.legend()
plt.grid()
plt.show()

# Definir valor de entrada
edad_simulacion = 30

# Calcular la membresía en los conjuntos difusos
membresia_joven = triangular(edad_simulacion, 0, 0, 50)
membresia_viejo = triangular(edad_simulacion, 50, 100, 100)

# Calcular el grado de activación de las reglas difusas
activacion_bajo = membresia_joven
activacion_alto = membresia_viejo

# Calcular la salida
salida_difusa = (activacion_bajo * bajo + activacion_alto * alto) / (activacion_bajo + activacion_alto)

# Visualizar el resultado
print("Edad:", edad_simulacion)
print("Valor de salida difusa:", salida_difusa)

# Visualización del resultado
plt.figure()
plt.plot(salida, bajo, label='Bajo')
plt.plot(salida, alto, label='Alto')
plt.plot(edad_simulacion, salida_difusa, 'ko', markersize=10, label='Valor de entrada')
plt.title('Conjuntos difusos para la variable de salida "salida" y valor de entrada')
plt.xlabel('Salida')
plt.ylabel('Membresía')
plt.legend()
plt.grid()
plt.show()
