#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 12/59 Inferencia Lógica: Unificación

import matplotlib.pyplot as plt

# Definición de los predicados y sus argumentos
p1 = ('padre', 'Juan', 'Pedro')
p2 = ('padre', 'Pedro', 'Carlos')
p3 = ('abuelo', 'X', 'Y')

# Función para unificar dos términos
def unificar(termino1, termino2):
    # Verificamos si los predicados son iguales
    if termino1[0] != termino2[0]:
        return None
    
    # Inicializamos un diccionario para almacenar las sustituciones
    sustituciones = {}
    
    # Iteramos sobre los argumentos de ambos predicados
    for arg1, arg2 in zip(termino1[1:], termino2[1:]):
        # Si los argumentos son diferentes y no son variables
        if arg1 != arg2 and (not arg1.islower() or not arg2.islower()):
            # La unificación falla
            return None
        # Si uno de los argumentos es una variable
        if arg1.islower() and arg2.islower():
            # Agregamos la sustitución al diccionario
            sustituciones[arg2] = arg1
    
    # Aplicamos las sustituciones al segundo término
    termino_unificado = [sustituciones.get(arg, arg) for arg in termino2]
    
    return tuple(termino_unificado)

# Ejemplo de unificación
resultado = unificar(p1, p3)
print("Unificación de p1 y p3:", resultado)

# Visualización gráfica
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title('Predicado 1: padre(Juan, Pedro)')
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, 'Juan\nPedro', ha='center', va='center', fontsize=14)
plt.subplot(1, 2, 2)
plt.title('Predicado 3: abuelo(X, Y)')
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, 'X\nY', ha='center', va='center', fontsize=14)
plt.show()
