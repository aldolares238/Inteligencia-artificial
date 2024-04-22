#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 27/59 Acciones, Situaciones y Eventos: Marcos

import matplotlib.pyplot as plt

# Creamos una lista de acciones
acciones = ['Leer', 'Escribir', 'Programar']

# Creamos una lista de situaciones
situaciones = ['En la biblioteca', 'En casa', 'En la oficina']

# Creamos una lista de eventos y asociamos acciones y situaciones
eventos = {
    ('Leer', 'En la biblioteca'): ['Concentración', 'Silencio'],
    ('Escribir', 'En casa'): ['Comodidad', 'Relajación'],
    ('Programar', 'En la oficina'): ['Productividad', 'Interacción']
}

# Función para obtener los eventos asociados a una acción y situación
def obtener_eventos(accion, situacion):
    return eventos.get((accion, situacion), [])

# Función para graficar los eventos asociados a una acción y situación
def graficar_eventos(accion, situacion):
    eventos_asociados = obtener_eventos(accion, situacion)
    plt.figure(figsize=(8, 5))
    plt.bar(range(len(eventos_asociados)), eventos_asociados, color='skyblue')
    plt.xlabel('Eventos')
    plt.ylabel('Importancia')
    plt.title(f'Eventos asociados a {accion} en {situacion}')
    plt.xticks(range(len(eventos_asociados)), eventos_asociados, rotation=45)
    plt.show()

# Ejemplo de uso
accion_ejemplo = 'Leer'
situacion_ejemplo = 'En la biblioteca'

# Mostramos los eventos asociados a la acción y situación especificadas
print(f'Eventos asociados a {accion_ejemplo} en {situacion_ejemplo}:')
print(obtener_eventos(accion_ejemplo, situacion_ejemplo))

# Graficamos los eventos asociados
graficar_eventos(accion_ejemplo, situacion_ejemplo)
