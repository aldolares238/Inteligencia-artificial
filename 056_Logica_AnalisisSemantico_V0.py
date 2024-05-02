#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 56/59 Analisis semantico

# Importar librerías necesarias
import matplotlib.pyplot as plt

# Definir la función de análisis semántico
def analisis_semantico(frase):
    # Aquí podríamos tener un análisis semántico más complejo,
    # pero para este ejemplo básico simplemente contaremos la cantidad de palabras
    palabras = frase.split()
    num_palabras = len(palabras)
    return num_palabras

# Pedir al usuario que ingrese una frase
frase_usuario = input("Ingrese una frase para análisis semántico: ")

# Realizar el análisis semántico
resultado = analisis_semantico(frase_usuario)

# Mostrar el resultado
print("El número de palabras en la frase es:", resultado)

# Visualización gráfica del análisis semántico
plt.bar(["Palabras"], [resultado], color='blue')
plt.xlabel('Tipo de análisis')
plt.ylabel('Cantidad')
plt.title('Análisis Semántico: Número de palabras en la frase')
plt.show()
