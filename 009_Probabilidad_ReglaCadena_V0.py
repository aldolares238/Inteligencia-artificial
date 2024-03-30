#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 8/60 Regla de la Cadena

import matplotlib.pyplot as plt

#Definimos las probabilidades de los eventos individuales
P_A = 0.6  #Probabilidad del evento A
P_B_dado_A = 0.8  #Probabilidad de B dado A

#Calculamos la probabilidad conjunta utilizando la Regla de la Cadena
P_A_y_B = P_A * P_B_dado_A

#Creamos un gráfico para visualizar las probabilidades
labels = ['P(A)', 'P(B|A)', 'P(A) * P(B|A)', 'P(A y B)']
probabilidades = [P_A, P_B_dado_A, P_A * P_B_dado_A, P_A_y_B]
#Le damos forma y colores a la grafica, ademas de etiquetas para el usuario
plt.bar(labels, probabilidades, color=['blue', 'green', 'orange', 'red'])
plt.title('Probabilidades utilizando la Regla de la Cadena')
plt.ylabel('Probabilidad')
plt.show()
#Imprimimos el resultado para el usuario
print("La probabilidad conjunta P(A y B) es:", P_A_y_B)
