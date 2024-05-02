#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 57/59 Gramática Causal Definida

# Importar librerías necesarias
import matplotlib.pyplot as plt

# Definir la función de Gramática Causal Definida
def gramatica_causal_definida(x):
    # La gramática causal definida puede ser cualquier función lógica o matemática.
    # En este ejemplo básico, simplemente definiremos una función lineal para demostrar el concepto.
    return 2 * x + 3

# Generar datos de entrada para la función
entrada = range(10)  # Generamos una secuencia del 0 al 9

# Aplicar la Gramática Causal Definida a cada entrada
salida = [gramatica_causal_definida(x) for x in entrada]

# Mostrar los resultados
print("Entrada:", list(entrada))
print("Salida:", salida)

# Visualización gráfica de la Gramática Causal Definida
plt.plot(entrada, salida, marker='o', color='blue', linestyle='-')
plt.xlabel('Entrada')
plt.ylabel('Salida')
plt.title('Gramática Causal Definida: Función lineal y = 2x + 3')
plt.grid(True)
plt.show()
