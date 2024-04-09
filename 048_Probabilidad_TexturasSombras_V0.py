#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 48/60 Texturas y Sombras

import numpy as np
import matplotlib.pyplot as plt

#Declaramos la función que modela la distribución de probabilidad de las texturas y sombras
def texturas_y_sombras(x):
    #Declaramos una distribución gaussiana para las texturas del ejemplo mostrado
    texturas = np.random.normal(loc=0, scale=1, size=x)
    #Suponemos una distribución uniforme para las sombras del ejemplo mostrado
    sombras = np.random.uniform(low=0, high=5, size=x)
    #La probabilidad de que un punto tenga textura es inversamente proporcional a la distancia a las sombras
    probabilidad_textura = 1 / (sombras + 1)
    #Calculamos el resultado combinando las texturas y las sombras con la probabilidad de textura
    resultado = texturas * probabilidad_textura
    return resultado

#Generamos los datos para nuestro ejemplo
x = np.linspace(0, 10, 100)
y = texturas_y_sombras(len(x))

#Graficamos al usuario los resultados
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Resultado Texturas y Sombras', color='blue')
plt.title('Ejemplo de Texturas y Sombras')
plt.xlabel('Distancia')
plt.ylabel('Intensidad')
plt.legend()
plt.grid(True)
plt.show()

