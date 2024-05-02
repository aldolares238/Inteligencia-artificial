#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 59/59!!!!!!!   Inducción Gramatical

import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
np.random.seed(0)
X = np.linspace(0, 5, 20)
Y = 2 * X + 1 + np.random.normal(0, 1, 20)

# Visualizar los datos
plt.scatter(X, Y, label='Datos de ejemplo')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Conjunto de datos')
plt.legend()
plt.show()

# Implementación del algoritmo de Inducción Gramatical para encontrar la mejor línea
def find_best_line(X, Y):
    # Inicializar los parámetros de la línea (pendiente y ordenada al origen)
    m = 0
    b = 0
    
    # Número máximo de iteraciones
    max_iterations = 1000
    
    # Tolerancia para la convergencia
    tolerance = 0.001
    
    # Tasa de aprendizaje
    learning_rate = 0.01
    
    # Iterar para ajustar la línea
    for _ in range(max_iterations):
        # Calcular las predicciones usando la línea actual
        predictions = m * X + b
        
        # Calcular el error
        error = np.mean((predictions - Y) ** 2)
        
        # Si el error es menor que la tolerancia, salir del bucle
        if error < tolerance:
            break
        
        # Calcular los gradientes
        gradient_m = 2 * np.mean((predictions - Y) * X)
        gradient_b = 2 * np.mean(predictions - Y)
        
        # Actualizar los parámetros de la línea
        m -= learning_rate * gradient_m
        b -= learning_rate * gradient_b
    
    return m, b

# Encontrar la mejor línea
m_best, b_best = find_best_line(X, Y)

# Visualizar la mejor línea
plt.scatter(X, Y, label='Datos de ejemplo')
plt.plot(X, m_best * X + b_best, color='red', label='Mejor línea')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Mejor línea ajustada')
plt.legend()
plt.show()

# Imprimir los parámetros de la mejor línea
print(f'Pendiente de la mejor línea: {m_best}')
print(f'Ordenada al origen de la mejor línea: {b_best}')
