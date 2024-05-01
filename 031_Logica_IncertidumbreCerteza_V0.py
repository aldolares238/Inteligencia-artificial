#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 31/59  Incertidumbre y Factores de Certeza

import matplotlib.pyplot as plt
import numpy as np

# Generamos datos aleatorios
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)  # Agregamos ruido para simular incertidumbre

# Creamos un gráfico para visualizar los datos
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Datos con incertidumbre', color='blue', alpha=0.5)  # Scatter plot para los datos

# Calculamos el factor de certeza para cada punto
certeza = np.abs(np.sin(x))  # Utilizamos la función seno como ejemplo de factor de certeza
certeza_normalized = certeza / certeza.max()  # Normalizamos los factores de certeza para que estén entre 0 y 1

# Añadimos los factores de certeza como colores al scatter plot
plt.scatter(x, y, c=certeza_normalized, cmap='viridis', label='Factores de Certeza')

# Añadimos leyendas y etiquetas
plt.colorbar(label='Factor de Certeza (normalizado)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Incertidumbre y Factores de Certeza')

# Mostramos el gráfico
plt.legend()
plt.grid(True)
plt.show()
