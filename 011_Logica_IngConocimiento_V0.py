#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 11/59 Ingeniería del Conocimiento

import matplotlib.pyplot as plt

# Definimos las reglas del sistema experto
def reglas():
    print("Reglas del sistema:")
    print("Si está lloviendo, llevar paraguas.")
    print("Si hace sol, llevar gafas de sol.")
    print("Si hace frío, llevar abrigo.")

# Función de inferencia
def inferencia(clima):
    if clima == "lluvia":
        return "paraguas"
    elif clima == "sol":
        return "gafas de sol"
    elif clima == "frío":
        return "abrigo"
    else:
        return "No se puede inferir."

# Función para graficar el resultado
def graficar(resultado):
    plt.bar(resultado.keys(), resultado.values())
    plt.xlabel('Objetos')
    plt.ylabel('Grado de pertenencia')
    plt.title('Inferencia de objetos según el clima')
    plt.show()

# Función principal
def main():
    # Mostrar las reglas del sistema
    reglas()

    # Pedir al usuario el estado del clima
    clima = input("Ingrese el estado del clima (lluvia/sol/frío): ")

    # Realizar inferencia
    objeto = inferencia(clima)

    # Mostrar resultado
    print("Según el clima,", objeto, "es recomendable.")

    # Graficar el resultado
    resultado = {objeto: 1}  # El grado de pertenencia es máximo (100%) para el objeto inferido
    graficar(resultado)

if __name__ == "__main__":
    main()
