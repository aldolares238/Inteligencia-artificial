#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 30/37 Teoría de Juegos: Equilibrios y Mecanismos

import numpy as np

#Definimos las estrategias de los jugadores
estrategias_jugador_1 = np.array([0.3, 0.7])  #Estrategias mixtas del jugador 1
estrategias_jugador_2 = np.array([0.6, 0.4])  #Estrategias mixtas del jugador 2

#Definimos las matrices de pagos
matriz_pago_jugador_1 = np.array([[3, 0], [5, 1]])  #Matriz de pagos del jugador 1
matriz_pago_jugador_2 = np.array([[3, 5], [0, 1]])  #Matriz de pagos del jugador 2

#Calculamos la utilidad esperada para el jugador 1
utilidad_esperada_jugador_1 = np.dot(estrategias_jugador_1, np.dot(matriz_pago_jugador_1, estrategias_jugador_2))

#Calculamos la utilidad esperada para el jugador 2
utilidad_esperada_jugador_2 = np.dot(estrategias_jugador_2, np.dot(matriz_pago_jugador_2, estrategias_jugador_1))

# Imprimimos los resultados
print("Utilidad esperada del Jugador 1:", utilidad_esperada_jugador_1)
print("Utilidad esperada del Jugador 2:", utilidad_esperada_jugador_2)

#Comprobamos si estamos en equilibrio de Nash
best_response_jugador_1 = np.argmax(np.dot(matriz_pago_jugador_1, estrategias_jugador_2))
best_response_jugador_2 = np.argmax(np.dot(matriz_pago_jugador_2.T, estrategias_jugador_1))
#Acorde los datos encontrados entre las respuestas de los jugadores se imprime un resultado
if best_response_jugador_1 == 0 and best_response_jugador_2 == 0:
    print("Equilibrio de Nash alcanzado: (No Saludar, No Saludar)")
elif best_response_jugador_1 == 0 and best_response_jugador_2 == 1:
    print("Equilibrio de Nash alcanzado: (No Saludar, Saludar)")
elif best_response_jugador_1 == 1 and best_response_jugador_2 == 0:
    print("Equilibrio de Nash alcanzado: (Saludar, No Saludar)")
else:
    print("Equilibrio de Nash alcanzado: (Saludar, Saludar)")


