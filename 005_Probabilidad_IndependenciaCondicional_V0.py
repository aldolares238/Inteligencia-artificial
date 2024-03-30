#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 5/60 - Independencia Condicional


import numpy as np
import matplotlib.pyplot as plt

#Definimos las probabilidades iniciales P(A), P(B) y P(C)
P_A = 0.6
P_B = 0.3
P_C = 0.8

#Calculamos probabilidad P(A|B) usando la fórmula de independencia condicional P(A|B) = P(A)
P_A_given_B = P_A

#Calculamos probabilidad P(C|B) usando la fórmula de independencia condicional P(C|B) = P(C)
P_C_given_B = P_C

#Calculamos P(A ∩ B)
P_A_intersect_B = P_A_given_B * P_B

#Calculamos P(C ∩ B)
P_C_intersect_B = P_C_given_B * P_B

#Mostramos los resultados al usuario
print("P(A|B):", P_A_given_B)
print("P(C|B):", P_C_given_B)
print("P(A ∩ B):", P_A_intersect_B)
print("P(C ∩ B):", P_C_intersect_B)

#Graficamos los eventos para mostrar al usuario
labels = ['A', 'B', 'C']
probabilities = [P_A, P_B, P_C]

plt.bar(labels, probabilities, color=['blue', 'orange', 'green'])
plt.xlabel('Eventos')
plt.ylabel('Probabilidades')
plt.title('Probabilidades de los eventos A, B y C')
plt.show()
