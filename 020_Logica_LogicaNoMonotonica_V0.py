#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 20/59 Lógica No Monotónica

import matplotlib.pyplot as plt

# Definimos las preferencias iniciales del usuario
preferencias_iniciales = {
    "vuelo_directo": True,
    "precio_bajo": True,
    "tiempo_corto": True
}

# Definimos las opciones de vuelo disponibles con sus características
opciones_vuelo = {
    "vuelo1": {"vuelo_directo": True, "precio": 200, "tiempo": 2},
    "vuelo2": {"vuelo_directo": False, "precio": 150, "tiempo": 3},
    "vuelo3": {"vuelo_directo": True, "precio": 180, "tiempo": 1}
}

# Función para evaluar las preferencias y seleccionar el mejor vuelo
def seleccionar_vuelo(preferencias, opciones):
    vuelo_seleccionado = None
    mejor_puntaje = -1  # Inicializamos el puntaje con un valor bajo

    for vuelo, caracteristicas in opciones.items():
        puntaje = 0

        # Aumentamos el puntaje si el vuelo cumple con las preferencias del usuario
        if caracteristicas["vuelo_directo"] == preferencias["vuelo_directo"]:
            puntaje += 1
        if caracteristicas["precio"] <= 200 and preferencias["precio_bajo"]:
            puntaje += 1
        if caracteristicas["tiempo"] <= 2 and preferencias["tiempo_corto"]:
            puntaje += 1

        # Si el puntaje supera al anterior, actualizamos el vuelo seleccionado
        if puntaje > mejor_puntaje:
            vuelo_seleccionado = vuelo
            mejor_puntaje = puntaje

    return vuelo_seleccionado

# Seleccionamos el vuelo según las preferencias del usuario
vuelo_elegido = seleccionar_vuelo(preferencias_iniciales, opciones_vuelo)

# Mostramos el vuelo elegido
print("El vuelo seleccionado es:", vuelo_elegido)

# Graficamos las opciones de vuelo
fig, ax = plt.subplots()

for vuelo, caracteristicas in opciones_vuelo.items():
    ax.scatter(caracteristicas["precio"], caracteristicas["tiempo"], label=vuelo)

ax.set_xlabel('Precio')
ax.set_ylabel('Tiempo')
ax.set_title('Opciones de vuelo')
ax.legend()
plt.show()

