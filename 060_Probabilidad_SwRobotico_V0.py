#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 60/60 SW Robótico

import numpy as np
import matplotlib.pyplot as plt

#Definimos los Parámetros del entorno
obstacle_poses = np.array([[3, 2], [1, 4], [-2, -3]])  #Declaramos las Posiciones de los obstáculos

#Definimos los Parámetros del robot
robot_pose = np.array([0, 0])  #Definimos la Pose inicial del robot
max_step_size = 1  #Declaramos el Tamaño máximo de paso del robot

#Declaramos el Tiempo de simulación
n_steps = 50  #Definimos el Número de pasos de la simulación

#Definimos la Simulación del movimiento del robot utilizando Random Walk
for step in range(n_steps):
    #Generamos un paso aleatorio para el robot
    step_size = np.random.uniform(0, max_step_size)
    step_angle = np.random.uniform(0, 2*np.pi)
    step_x = step_size * np.cos(step_angle)
    step_y = step_size * np.sin(step_angle)
    
    #Actualizamos la posición del robot
    new_pose = robot_pose + np.array([step_x, step_y])
    
    #Verificamos si la nueva posición del robot colisiona con algún obstáculo
    collision = False
    for obstacle_pose in obstacle_poses:
        distance = np.linalg.norm(new_pose - obstacle_pose)
        if distance < 1:  # Radio de colisión
            collision = True
            break
    
    #Si no hay colisión, actualiza la posición del robot
    if not collision:
        robot_pose = new_pose
    
    #Visualización de la simulación
    plt.clf()
    plt.plot(obstacle_poses[:, 0], obstacle_poses[:, 1], 'ks', label='Obstáculos')
    plt.plot(robot_pose[0], robot_pose[1], 'ro', label='Robot')
    plt.xlabel('Posición en x')
    plt.ylabel('Posición en y')
    plt.title('Simulación de Robot Móvil con Random Walk')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.pause(0.1)

plt.show()
