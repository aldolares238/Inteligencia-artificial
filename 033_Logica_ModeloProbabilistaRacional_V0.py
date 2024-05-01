#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 33/59 Modelo Probabilista Racional

import numpy as np
import matplotlib.pyplot as plt

# Definimos la función de actualización del Modelo Probabilista Racional
def actualizar_probabilidad(prior_probabilidad, likelihood):
    # La nueva probabilidad es el producto del prior y la verosimilitud
    posterior_probabilidad = prior_probabilidad * likelihood
    # Verificamos si la suma de las probabilidades es cero
    if np.sum(posterior_probabilidad) == 0:
        return posterior_probabilidad
    # Normalizamos para asegurarnos de que la suma de las probabilidades sea 1
    posterior_probabilidad /= np.sum(posterior_probabilidad)
    return posterior_probabilidad

# Creamos un conjunto de datos de ejemplo
datos = np.array([0, 1, 1, 0, 1, 1, 1, 0, 1, 1])

# Inicializamos la probabilidad a priori, asumiendo una distribución uniforme
prior_probabilidad = np.ones(2) / 2

# Definimos la verosimilitud (likelihood) basada en los datos observados
def calcular_likelihood(valor, dato):
    return valor ** dato * (1 - valor) ** (1 - dato)

# Creamos un rango de valores de probabilidad a evaluar
valores_probabilidad = np.linspace(0, 1, 100)

# Calculamos la probabilidad posterior para cada valor de probabilidad
posterior_probabilidades = []
for valor in valores_probabilidad:
    likelihood = np.prod(calcular_likelihood(valor, datos))
    posterior = actualizar_probabilidad(prior_probabilidad, likelihood)
    posterior_probabilidades.append(posterior)

# Convertimos la lista de probabilidades en un array de numpy
posterior_probabilidades = np.array(posterior_probabilidades)

# Graficamos los resultados
plt.plot(valores_probabilidad, posterior_probabilidades[:, 0], label='Probabilidad Posterior de 0')
plt.plot(valores_probabilidad, posterior_probabilidades[:, 1], label='Probabilidad Posterior de 1')
plt.xlabel('Probabilidad')
plt.ylabel('Densidad de Probabilidad')
plt.title('Modelo Probabilista Racional')
plt.legend()
plt.show()
