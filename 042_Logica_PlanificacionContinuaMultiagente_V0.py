#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 42/59 Planificación Continua y Multiagente
import matplotlib.pyplot as plt

# Creamos una clase para representar los agentes
class Agente:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion

# Función para mostrar el estado inicial de los agentes
def mostrar_estado(agentes):
    for agente in agentes:
        print(f"{agente.nombre}: {agente.posicion}")

# Función para simular el movimiento de los agentes
def mover_agentes(agentes, destinos):
    for agente, destino in zip(agentes, destinos):
        agente.posicion = destino

# Función para visualizar el movimiento de los agentes usando Matplotlib
def visualizar_movimiento(agentes):
    posiciones = [agente.posicion for agente in agentes]
    nombres = [agente.nombre for agente in agentes]

    plt.figure(figsize=(8, 6))
    plt.barh(nombres, posiciones, color='skyblue')
    plt.xlabel('Posición')
    plt.ylabel('Agente')
    plt.title('Movimiento de los agentes')
    plt.grid(True)
    plt.show()

# Crear agentes
agente1 = Agente("Agente 1", 0)
agente2 = Agente("Agente 2", 0)

# Mostrar estado inicial de los agentes
print("Estado inicial:")
mostrar_estado([agente1, agente2])

# Definir destinos de los agentes
destinos_agente1 = [3, 5, 8]
destinos_agente2 = [2, 4, 7]

# Simular movimiento de los agentes
mover_agentes([agente1, agente2], destinos_agente1)

# Mostrar estado después del primer movimiento
print("\nDespués del primer movimiento:")
mostrar_estado([agente1, agente2])

# Visualizar el primer movimiento
visualizar_movimiento([agente1, agente2])

# Simular segundo movimiento de los agentes
mover_agentes([agente1, agente2], destinos_agente2)

# Mostrar estado después del segundo movimiento
print("\nDespués del segundo movimiento:")
mostrar_estado([agente1, agente2])

# Visualizar el segundo movimiento
visualizar_movimiento([agente1, agente2])
