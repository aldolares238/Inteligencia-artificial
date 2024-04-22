#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 21/59 Lógica por Defecto

import matplotlib.pyplot as plt

# Creamos una función que simula el proceso de inferencia lógica por defecto
def logica_por_defecto(edad, ingreso):
    # Regla 1: Si la edad es menor de 30 y el ingreso es alto, entonces es probable que sea un estudiante universitario.
    if edad < 30 and ingreso > 50000:
        return "Estudiante universitario"
    # Regla 2: Si la edad es mayor o igual a 30 y el ingreso es bajo, entonces es probable que sea un trabajador.
    elif edad >= 30 and ingreso < 30000:
        return "Trabajador"
    # Regla 3: En cualquier otro caso, no podemos hacer una inferencia clara.
    else:
        return "Indefinido"

# Datos de ejemplo: edad e ingreso
edad = 25
ingreso = 60000

# Realizamos la inferencia utilizando la función logica_por_defecto
resultado = logica_por_defecto(edad, ingreso)

# Imprimimos el resultado
print("Resultado de la inferencia:", resultado)

# Visualización gráfica del resultado
plt.figure(figsize=(6, 4))
plt.bar(resultado, 1, color='blue')
plt.title("Resultado de la inferencia")
plt.xlabel("Categoría")
plt.ylabel("Probabilidad")
plt.show()
