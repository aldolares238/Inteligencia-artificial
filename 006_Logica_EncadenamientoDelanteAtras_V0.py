#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 6/59 Encadenamiento: Hacia Delante y Atrás

import networkx as nx
import matplotlib.pyplot as plt

# Definición de la base de conocimientos de reglas y hechos
base_conocimientos = {
    "Reglas": {
        "R1": ("si Perro es Mamífero entonces Caliente", ["Perro es Mamífero"]),
        "R2": ("si Gato es Mamífero entonces Caliente", ["Gato es Mamífero"]),
        "R3": ("si Vaca es Mamífero entonces Caliente", ["Vaca es Mamífero"]),
        "R4": ("si Pájaro es Vertebrado entonces Caliente", ["Pájaro es Vertebrado"]),
        "R5": ("si Tiburón es Vertebrado entonces Caliente", ["Tiburón es Vertebrado"]),
        "R6": ("si Ballena es Vertebrado entonces Caliente", ["Ballena es Vertebrado"]),
        "R7": ("si Caliente entonces Animal", ["Caliente"]),
    },
    "Hechos": [],
}

# Función para encadenamiento hacia adelante
def encadenamiento_hacia_adelante(base_conocimientos):
    nuevos_hechos = True
    while nuevos_hechos:
        nuevos_hechos = False
        for regla, (implicacion, antecedentes) in base_conocimientos["Reglas"].items():
            if all(antecedente in base_conocimientos["Hechos"] for antecedente in antecedentes) and implicacion not in base_conocimientos["Hechos"]:
                base_conocimientos["Hechos"].append(implicacion)
                nuevos_hechos = True
                print(f"Se activó la regla {regla}: {implicacion}")
    print("Hechos deducidos:", base_conocimientos["Hechos"])
    # Visualización
    visualizar_base_conocimientos(base_conocimientos)

# Función para visualizar la base de conocimientos
def visualizar_base_conocimientos(base_conocimientos):
    G = nx.DiGraph()
    for regla, (implicacion, antecedentes) in base_conocimientos["Reglas"].items():
        for antecedente in antecedentes:
            G.add_edge(antecedente, implicacion)

    pos = nx.spring_layout(G)  # Posiciones de los nodos
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
    plt.title('Base de Conocimientos')
    plt.show()

# Ejecutar encadenamiento hacia adelante
print("Encadenamiento hacia adelante:")
encadenamiento_hacia_adelante(base_conocimientos)

