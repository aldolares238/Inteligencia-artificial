#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 16/37 - Búsqueda Online


import random  # Importa la biblioteca random para generar números aleatorios

# Función objetivo: comprueba si el número generado coincide con el objetivo
def verificar_objetivo(objetivo, numero_generado):
    if numero_generado == objetivo:
        return True
    else:
        return False

# Implementación de la Búsqueda en Línea
def busqueda_en_linea(objetivo, max_intentos):
    intentos_realizados = 0  # Contador de intentos realizados
    encontrado = False  # Bandera para indicar si se encontró el objetivo
    
    # Realiza la búsqueda hasta alcanzar el máximo de intentos o encontrar el objetivo
    while intentos_realizados < max_intentos and not encontrado:
        # Genera un número aleatorio como supuesta solución
        numero_generado = random.randint(1, 30)  # Genera un número aleatorio entre 1 y 30
        
        # Verifica si el número generado coincide con el objetivo
        encontrado = verificar_objetivo(objetivo, numero_generado)
        
        # Incrementa el contador de intentos
        intentos_realizados += 1
    
    return encontrado, intentos_realizados

# Parámetros
objetivo_a_buscar = 5  # Número que se desea encontrar
max_intentos = 20      # Número máximo de intentos permitidos

# Ejecuta la búsqueda en línea
resultado, intentos = busqueda_en_linea(objetivo_a_buscar, max_intentos)

# Imprime el resultado de la búsqueda
if resultado:
    print(f"¡Se encontró el número {objetivo_a_buscar} en {intentos} intentos!")
else:
    print(f"No se encontró el número {objetivo_a_buscar} después de {intentos} intentos.")
