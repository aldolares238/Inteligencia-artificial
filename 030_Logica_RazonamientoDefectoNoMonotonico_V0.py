#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 30/59 Razonamiento por Defecto y No Monotónico

import matplotlib.pyplot as plt

# Creamos una función para calcular la regla de inferencia por defecto
def razonamiento_defecto(x):
    if x < 5:
        return True
    else:
        return False

# Creamos una función para calcular la regla de inferencia no monotónica
def razonamiento_no_monotónico(x):
    if x < 7:
        return True
    else:
        return False

# Creamos una lista de valores para x
x_values = list(range(1, 11))

# Creamos una lista para almacenar los resultados de razonamiento por defecto
resultados_defecto = []

# Aplicamos la regla de inferencia por defecto a cada valor de x y almacenamos los resultados
for x in x_values:
    resultados_defecto.append(razonamiento_defecto(x))

# Creamos una lista para almacenar los resultados de razonamiento no monotónico
resultados_no_monotónico = []

# Aplicamos la regla de inferencia no monotónica a cada valor de x y almacenamos los resultados
for x in x_values:
    resultados_no_monotónico.append(razonamiento_no_monotónico(x))

# Creamos una figura para mostrar los resultados
plt.figure(figsize=(10, 5))

# Graficamos los resultados de razonamiento por defecto
plt.subplot(1, 2, 1)
plt.plot(x_values, resultados_defecto, marker='o')
plt.title('Razonamiento por Defecto')
plt.xlabel('x')
plt.ylabel('Resultado')
plt.xticks(x_values)
plt.grid(True)

# Graficamos los resultados de razonamiento no monotónico
plt.subplot(1, 2, 2)
plt.plot(x_values, resultados_no_monotónico, marker='o')
plt.title('Razonamiento No Monotónico')
plt.xlabel('x')
plt.ylabel('Resultado')
plt.xticks(x_values)
plt.grid(True)

# Mostramos la figura
plt.tight_layout()
plt.show()
