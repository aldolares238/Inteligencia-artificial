#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 19/59 Lógica Temporal

import matplotlib.pyplot as plt

# Definimos una función para determinar el estado de la lámpara en un momento específico
def lamp_state(time):
    if time < 12:
        return "Apagada"
    else:
        return "Encendida"

# Creamos una lista de tiempos para simular un intervalo de tiempo de 24 horas
times = range(24)

# Creamos una lista de estados de la lámpara para cada momento en la lista de tiempos
lamp_states = [lamp_state(time) for time in times]

# Creamos el gráfico de barras para visualizar el estado de la lámpara a lo largo del día
plt.bar(times, [1 if state == "Encendida" else 0 for state in lamp_states], color='blue', width=0.5)

# Configuramos el eje x
plt.xticks(range(0, 25, 2))

# Etiquetas y título del gráfico
plt.xlabel('Hora del día')
plt.ylabel('Estado de la lámpara')
plt.title('Estado de la lámpara a lo largo del día')

# Mostramos el gráfico
plt.show()
