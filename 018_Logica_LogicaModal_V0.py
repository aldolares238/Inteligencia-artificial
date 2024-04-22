#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 18/59 Lógica Modal

import matplotlib.pyplot as plt

# Función para calcular la verdad de una fórmula modal
def evaluar_formula_modal(formula):
    # Supongamos que la fórmula es simplemente una proposición P
    # Y la verdad de P está representada por un valor booleano
    verdad_de_P = True  # Cambiar esto según la verdad de P
    if formula == '□P':  # Si la fórmula es una necesidad de P
        return verdad_de_P  # Devolver la verdad de P
    elif formula == '◊P':  # Si la fórmula es una posibilidad de P
        return verdad_de_P  # Devolver la verdad de P

# Fórmula a evaluar
formula = '□P'  # Cambiar la fórmula según sea necesario

# Evaluar la fórmula y obtener el resultado
resultado = evaluar_formula_modal(formula)

# Crear un gráfico para mostrar el resultado
plt.figure(figsize=(4, 4))
plt.axis('off')

# Mostrar el resultado de manera gráfica
if resultado:
    plt.text(0.5, 0.5, "Verdadero", ha='center', va='center', fontsize=20, color='green')
else:
    plt.text(0.5, 0.5, "Falso", ha='center', va='center', fontsize=20, color='red')

# Mostrar el gráfico
plt.show()
