#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 48/59 Mejor Hipótesis Actual

import matplotlib.pyplot as plt

# Creamos una función para calcular el error cuadrático medio entre dos listas de valores
def calcular_error(hypothesis, target):
    total_error = 0
    for i in range(len(hypothesis)):
        total_error += (hypothesis[i] - target[i]) ** 2
    return total_error / len(hypothesis)

# Datos de entrada: características (x) y valores objetivo (y)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Inicializamos una hipótesis aleatoria (en este caso, una línea con pendiente 1 y ordenada al origen 0)
m_current = 1
b_current = 0

# Hiperparámetro: tasa de aprendizaje
learning_rate = 0.01

# Número de iteraciones para ajustar la hipótesis
num_iterations = 100

# Listas para almacenar el error y los parámetros de la hipótesis en cada iteración
errors = []
m_values = []
b_values = []

# Iteramos para ajustar la hipótesis
for i in range(num_iterations):
    # Calculamos la predicción actual de la hipótesis
    predicted_values = [m_current * xi + b_current for xi in x]
    
    # Calculamos el error actual
    error = calcular_error(predicted_values, y)
    errors.append(error)
    
    # Actualizamos los parámetros de la hipótesis usando el gradiente descendente
    m_gradient = 0
    b_gradient = 0
    for j in range(len(x)):
        m_gradient += (predicted_values[j] - y[j]) * x[j]
        b_gradient += (predicted_values[j] - y[j])
    m_gradient *= (2 / len(x))
    b_gradient *= (2 / len(x))
    
    m_current -= learning_rate * m_gradient
    b_current -= learning_rate * b_gradient
    
    # Guardamos los valores de los parámetros en cada iteración
    m_values.append(m_current)
    b_values.append(b_current)

# Mostramos la evolución del error
plt.plot(range(num_iterations), errors)
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.title('Error over Iterations')
plt.show()

# Mostramos la evolución de los parámetros de la hipótesis
plt.plot(range(num_iterations), m_values, label='Slope (m)')
plt.plot(range(num_iterations), b_values, label='Intercept (b)')
plt.xlabel('Iterations')
plt.ylabel('Parameter Value')
plt.title('Parameter Values over Iterations')
plt.legend()
plt.show()

# Graficamos la hipótesis final sobre los datos de entrada
final_predicted_values = [m_current * xi + b_current for xi in x]
plt.scatter(x, y, label='Actual Data')
plt.plot(x, final_predicted_values, color='red', label='Final Hypothesis')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Final Hypothesis')
plt.legend()
plt.show()
