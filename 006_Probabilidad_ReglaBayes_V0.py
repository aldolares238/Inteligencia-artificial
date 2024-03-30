#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 6/60 Regla de Bayes


import numpy as np
import matplotlib.pyplot as plt

#Definimos las probabilidades a priori y condicionales, P(A) y P(B|A)
p_A = 0.3
p_B_dado_A = 0.8

#Calculamos la probabilidad complementaria P(A') y P(B|A')
p_A_complementaria = 1 - p_A
p_B_dado_A_complementaria = 0.4

#Calculamos la probabilidad marginal P(B)
p_B = p_B_dado_A * p_A + p_B_dado_A_complementaria * p_A_complementaria

#Clculamos la probabilidad posterior P(A|B) usando la Regla de Bayes
p_A_dado_B = (p_B_dado_A * p_A) / p_B

#Imprimimos el resultado para el usuario
print("La probabilidad de A dado B es:", p_A_dado_B)

#Visualización gráfica al usuario
labels = ['P(A)', 'P(A\')']
prior_probabilities = [p_A, p_A_complementaria]
colors = ['#ff9999', '#66b3ff']
#Agregamos figuras para la visualizacion y damos estetica
plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.pie(prior_probabilities, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Probabilidades a priori')
#Toda grafica necesita etiquetas de apoyo para su comprension
labels = ['P(B|A)', 'P(B|A\')']
conditional_probabilities = [p_B_dado_A, p_B_dado_A_complementaria]
colors = ['#ff9999', '#66b3ff']
#Mostramos los resultados de las probabilidaedss
plt.subplot(1, 2, 2)
plt.pie(conditional_probabilities, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Probabilidades condicionales')
plt.tight_layout()
plt.show()
