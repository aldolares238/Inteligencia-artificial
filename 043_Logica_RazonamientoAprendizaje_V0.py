#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 43/59 Tipos de Razonamiento y Aprendizaje

import matplotlib.pyplot as plt

# Definimos los datos de entrada
entradas = [0, 1, 2, 3, 4, 5]
salidas = [0, 1, 4, 9, 16, 25]

# Creamos una función para el razonamiento y aprendizaje
def razonamiento_aprendizaje(entradas, salidas):
    # Inicializamos los pesos
    peso = 0.5
    # Inicializamos la tasa de aprendizaje
    tasa_aprendizaje = 0.01
    # Inicializamos el número de iteraciones
    iteraciones = 50

    # Iteramos para ajustar los pesos
    for _ in range(iteraciones):
        for entrada, salida in zip(entradas, salidas):
            # Calculamos la predicción
            prediccion = entrada * peso
            # Calculamos el error
            error = (prediccion - salida) ** 2
            # Ajustamos el peso
            peso -= (prediccion - salida) * entrada * tasa_aprendizaje

    return peso

# Calculamos el peso optimizado
peso_optimizado = razonamiento_aprendizaje(entradas, salidas)

# Creamos una función para visualizar los resultados
def visualizar_resultados(entradas, salidas, peso_optimizado):
    # Creamos una figura y ejes
    fig, ax = plt.subplots()
    # Graficamos los datos de entrada y salida
    ax.plot(entradas, salidas, 'bo', label='Datos de entrenamiento')
    # Graficamos la línea de predicción
    ax.plot(entradas, [x * peso_optimizado for x in entradas], 'r-', label='Predicción')
    # Etiquetas de los ejes
    ax.set_xlabel('Entrada')
    ax.set_ylabel('Salida')
    # Título de la gráfica
    ax.set_title('Razonamiento y Aprendizaje')
    # Leyenda
    ax.legend()
    # Mostramos la gráfica
    plt.show()

# Visualizamos los resultados
visualizar_resultados(entradas, salidas, peso_optimizado)
