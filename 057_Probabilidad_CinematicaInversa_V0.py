#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 57/60 Cinematica inversa

import numpy as np
import matplotlib.pyplot as plt

#Definimos la función de cinemática directa para calcular la posición del extremo del brazo
def forward_kinematics(theta1, theta2):
    #Declaramos Longitudes de los eslabones del brazo
    l1 = 5  #Declaramos Longitud del primer eslabón
    l2 = 3  #Declaramos Longitud del segundo eslabón
    
    #Calculamos las coordenadas (x, y) del extremo del brazo
    x = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    y = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)
    
    return x, y

#Definimos la función de cinemática inversa para calcular los ángulos del brazo a partir de una posición deseada
def inverse_kinematics(x_desired, y_desired, num_samples=1000):
    # Rango de ángulos posibles para las articulaciones
    min_theta = 0
    max_theta = np.pi
    
    #Generamos muestras aleatorias de ángulos para theta1 y theta2
    theta1_samples = np.random.uniform(min_theta, max_theta, num_samples)
    theta2_samples = np.random.uniform(min_theta, max_theta, num_samples)
    
    #Calculamos las coordenadas (x, y) para cada muestra
    x_samples, y_samples = forward_kinematics(theta1_samples, theta2_samples)
    
    #Calculamos la distancia euclidiana entre la posición deseada y las muestras generadas
    distances = np.sqrt((x_samples - x_desired)**2 + (y_samples - y_desired)**2)
    
    #Encontramos el índice de la muestra con la distancia mínima
    min_index = np.argmin(distances)
    
    #Se devuelven los ángulos correspondientes a la muestra con la distancia mínima
    return theta1_samples[min_index], theta2_samples[min_index]

#Definmos la posición deseada del extremo del brazo
x_desired = 6
y_desired = 4

#Calculamos los ángulos para alcanzar la posición deseada
theta1, theta2 = inverse_kinematics(x_desired, y_desired)

#mostramos los resultados
print("Ángulos para alcanzar la posición deseada:")
print("Theta1:", np.degrees(theta1), "grados")
print("Theta2:", np.degrees(theta2), "grados")

#Graficamos el brazo robótico y la posición deseada
plt.figure(figsize=(6, 6))
plt.plot([0, forward_kinematics(theta1, theta2)[0]], [0, forward_kinematics(theta1, theta2)[1]], 'b-o', label='Brazo Robótico')
plt.plot(x_desired, y_desired, 'r*', markersize=10, label='Posición Deseada')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cinemática Inversa con Enfoque Probabilístico')
plt.axis('equal')
plt.legend()
plt.grid(True)
plt.show()
