#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 52/59 Programación Lógica Inductiva: FOIL

import matplotlib.pyplot as plt

# Creamos datos de ejemplo
datos = {
    'sunny': {'hot': 85, 'cold': 60},
    'overcast': {'hot': 83, 'cold': 58},
    'rainy': {'hot': 70, 'cold': 65}
}

# Visualizamos los datos
fig, ax = plt.subplots()

# Plot de datos
for key, value in datos.items():
    ax.scatter([key] * len(value), list(value.values()), label=key)

# Configuración de la gráfica
ax.set_xlabel('Weather')
ax.set_ylabel('Temperature')
ax.set_title('FOIL Example: Weather and Temperature')
ax.legend()
plt.xticks(rotation=45)

plt.show()
