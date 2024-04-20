#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 2/59 Base de Conocimiento

# Definimos la base de conocimiento como un diccionario donde las claves son hechos y los valores son las conclusiones
base_conocimiento = {
    ("llueve", "lunes"): "necesito un paraguas",
    ("soleado", "sábado"): "es un buen día para ir a la playa",
    ("nublado", "domingo"): "podría hacer fresco, mejor llevar un suéter"
}

# Definimos una función para consultar la base de conocimiento y obtener una conclusión
def consultar_base_conocimiento(clima, dia):
    for hechos, conclusion in base_conocimiento.items():
        if clima == hechos[0] and dia == hechos[1]:
            return conclusion
    return "No se encontró información para el clima y día especificados"

# Pedimos al usuario que ingrese el clima y el día
clima_usuario = input("Ingrese el clima (llueve/soleado/nublado): ")
dia_usuario = input("Ingrese el día de la semana: ")

# Consultamos la base de conocimiento
resultado = consultar_base_conocimiento(clima_usuario, dia_usuario)

# Mostramos el resultado al usuario
print("Resultado de la consulta:", resultado)

