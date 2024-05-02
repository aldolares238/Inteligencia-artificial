#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 58/59 Ambigüedad

# Importar librerías necesarias
import matplotlib.pyplot as plt
import numpy as np

# Definir la función para manejar la ambigüedad
def manejar_ambiguedad(x):
    # La ambigüedad puede surgir en diferentes contextos, como la interpretación de un valor incierto.
    # En este ejemplo básico, vamos a definir una función que muestre dos posibles interpretaciones
    # de un valor dado, una más conservadora y otra más optimista.
    valor_conservador = x * 0.8
    valor_optimista = x * 1.2
    return valor_conservador, valor_optimista

# Generar datos de entrada
entrada = np.linspace(0, 10, 100)  # Creamos una secuencia de valores de 0 a 10

# Aplicar la función para manejar la ambigüedad a cada entrada
salida_conservadora = []
salida_optimista = []
for x in entrada:
    conservador, optimista = manejar_ambiguedad(x)
    salida_conservadora.append(conservador)
    salida_optimista.append(optimista)

# Mostrar los resultados
print("Entrada:", list(entrada))
print("Salida Conservadora:", salida_conservadora)
print("Salida Optimista:", salida_optimista)

# Visualización gráfica de la ambigüedad
plt.plot(entrada, salida_conservadora, label='Conservador', color='red')
plt.plot(entrada, salida_optimista, label='Optimista', color='green')
plt.xlabel('Entrada')
plt.ylabel('Salida')
plt.title('Manejo de Ambigüedad: Dos interpretaciones posibles')
plt.legend()
plt.grid(True)
plt.show()
