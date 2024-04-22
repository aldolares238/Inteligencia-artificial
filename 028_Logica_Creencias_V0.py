#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 28/59 Eventos y Objetos Mentales: Creencias

import matplotlib.pyplot as plt

class Creencia:
    def __init__(self, ciudad, clima, temperatura):
        self.ciudad = ciudad  # Nombre de la ciudad
        self.clima = clima  # Condición climática
        self.temperatura = temperatura  # Temperatura actual

    def __str__(self):
        return f"{self.ciudad}: {self.clima}, {self.temperatura}°C"  # Representación en cadena de la creencia

class BaseConocimiento:
    def __init__(self):
        self.creencias = []  # Lista para almacenar las creencias

    def agregar_creencia(self, creencia):
        self.creencias.append(creencia)  # Agrega una nueva creencia a la lista

    def consultar_creencias(self):
        for creencia in self.creencias:
            print(creencia)  # Imprime cada creencia en la lista

# Crear una base de conocimiento
bc = BaseConocimiento()

# Agregar creencias a la base de conocimiento
bc.agregar_creencia(Creencia("Ciudad A", "Soleado", 28))  
bc.agregar_creencia(Creencia("Ciudad B", "Lluvioso", 15))  
bc.agregar_creencia(Creencia("Ciudad C", "Nublado", 20))  

# Consultar las creencias en la base de conocimiento
print("Condiciones climáticas actuales:")
bc.consultar_creencias()

# Mostrar gráficamente las temperaturas de las ciudades
ciudades = [creencia.ciudad for creencia in bc.creencias]
temperaturas = [creencia.temperatura for creencia in bc.creencias]

plt.bar(ciudades, temperaturas, color='skyblue')
plt.xlabel('Ciudades')
plt.ylabel('Temperatura (°C)')
plt.title('Temperaturas Actuales')
plt.xticks(rotation=45)
plt.show()
