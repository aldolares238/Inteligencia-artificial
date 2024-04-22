#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 17/59 - Lógicas de Orden Superior

from functools import reduce
import matplotlib.pyplot as plt

# Definición de funciones de puertas lógicas

# Función de AND
def AND(*args):
    """
    Función que simula la operación lógica AND entre un número variable de entradas.

    :param args: Entradas a las cuales aplicar la operación AND.
    :return: True si todas las entradas son True, False en caso contrario.
    """
    return reduce(lambda x, y: x and y, args)

# Función de OR
def OR(*args):
    """
    Función que simula la operación lógica OR entre un número variable de entradas.

    :param args: Entradas a las cuales aplicar la operación OR.
    :return: True si al menos una de las entradas es True, False en caso contrario.
    """
    return reduce(lambda x, y: x or y, args)

# Función de NOT
def NOT(x):
    """
    Función que simula la operación lógica NOT.

    :param x: Valor al cual aplicar la operación NOT.
    :return: True si x es False, False si x es True.
    """
    return not x

# Ejemplo de uso de puertas lógicas para simular un circuito

# Definimos las entradas
entrada_1 = True
entrada_2 = False

# Aplicamos las puertas lógicas para obtener resultados
resultado_and = AND(entrada_1, NOT(entrada_2))
resultado_or = OR(entrada_1, entrada_2)

# Mostramos los resultados gráficamente
plt.figure(figsize=(8, 4))

# Configuramos el gráfico para la puerta AND
plt.subplot(1, 2, 1)
plt.title('Puerta AND')
plt.axis('off')  # Ocultamos los ejes
plt.text(0.5, 0.6, f'Entrada 1: {entrada_1}\nEntrada 2: {NOT(entrada_2)}\nResultado: {resultado_and}',
         horizontalalignment='center', verticalalignment='center')

# Configuramos el gráfico para la puerta OR
plt.subplot(1, 2, 2)
plt.title('Puerta OR')
plt.axis('off')  # Ocultamos los ejes
plt.text(0.5, 0.6, f'Entrada 1: {entrada_1}\nEntrada 2: {entrada_2}\nResultado: {resultado_or}',
         horizontalalignment='center', verticalalignment='center')

plt.tight_layout()  # Ajustamos el diseño para evitar superposiciones
plt.show()
