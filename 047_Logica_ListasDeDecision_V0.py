#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 47/59 Listas de Decisión: K-DL y K-DT

import matplotlib.pyplot as plt

# Definición de la función de decisión
def decision_list(features):
    # Si la primera característica es 'A', devolver 1
    if features[0] == 'A':
        return 1
    # Si la segunda característica es 'B', devolver 0
    elif features[1] == 'B':
        return 0
    # Si no se cumple ninguna de las condiciones anteriores, devolver 1
    else:
        return 1

# Ejemplo de características
example_features = ['A', 'C']

# Aplicar la función de decisión al ejemplo
result = decision_list(example_features)

# Imprimir el resultado
print("El resultado de las características", example_features, "es:", result)

# Crear un gráfico que muestre las características y el resultado
plt.figure(figsize=(6, 4))
plt.bar(range(len(example_features)), [1 if feature == 'A' else 0 for feature in example_features], color='blue')
plt.xticks(range(len(example_features)), example_features)
plt.title('Características y Resultado')
plt.xlabel('Características')
plt.ylabel('Valor (1 o 0)')
plt.ylim(0, 1)
plt.show()
