#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 15/59 Resolución: Skolem

import matplotlib.pyplot as plt

# Definimos una función para aplicar el algoritmo de resolución Skolem
def resolucion_skolem(clausulas):
    nueva_clausula = set()
    while True:
        for i in range(len(clausulas)):
            for j in range(i+1, len(clausulas)):
                resolvente = clausulas[i].union(clausulas[j])
                resolvente_copy = resolvente.copy()  # Creamos una copia del conjunto
                for literal in resolvente_copy:     # Iteramos sobre la copia
                    negacion_literal = "-" + literal if literal[0] != "-" else literal[1:]
                    if literal in resolvente and negacion_literal in resolvente:
                        resolvente.remove(literal)
                        resolvente.remove(negacion_literal)
                if len(resolvente) == len(clausulas[i]) - 1:
                    return True, resolvente
        return False, nueva_clausula

# Definimos las clausulas de ejemplo
clausulas = [set(["P", "-Q"]), set(["-P", "R"]), set(["-R", "Q"])]

# Aplicamos el algoritmo de resolución Skolem
es_valido, resolvente = resolucion_skolem(clausulas)

# Mostramos el resultado
if es_valido:
    print("La fórmula es válida.")
    print("Resolvente:", resolvente)
else:
    print("La fórmula no es válida.")

# Graficamos el resultado
plt.figure(figsize=(5,5))
plt.axis('off')

if es_valido:
    plt.text(0.5, 0.5, "Válido", fontsize=20, ha='center')
else:
    plt.text(0.5, 0.5, "No válido", fontsize=20, ha='center')

plt.show()
