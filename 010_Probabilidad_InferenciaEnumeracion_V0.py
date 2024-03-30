#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 10/60 Inferencia por Enumeración

import numpy as np
import matplotlib.pyplot as plt

#Definimos las probabilidades de las variables
#Probabilidad de que el cielo esté nublado
p_nublado = 0.5
#Probabilidad de que el pasto esté mojado dado que el cielo está nublado
p_mojado_dado_nublado = 0.9
#Probabilidad de que el pasto esté mojado dado que el cielo no está nublado
p_mojado_dado_no_nublado = 0.2

#Función de inferencia por enumeración
def inferencia_por_enumeracion(p_nublado, p_mojado_dado_nublado, p_mojado_dado_no_nublado):
    # alculamos la probabilidad de que el pasto esté mojado
    p_mojado = p_nublado * p_mojado_dado_nublado + (1 - p_nublado) * p_mojado_dado_no_nublado
    #Calculamos la probabilidad de que el cielo esté nublado dado que el pasto está mojado
    p_nublado_dado_mojado = (p_nublado * p_mojado_dado_nublado) / p_mojado
    return p_nublado_dado_mojado

#Realizamos la inferencia
probabilidad_nublado_dado_mojado = inferencia_por_enumeracion(p_nublado, p_mojado_dado_nublado, p_mojado_dado_no_nublado)
print("Probabilidad de que el cielo esté nublado dado que el pasto está mojado:", probabilidad_nublado_dado_mojado)

#Creamos un gráfico de barras para visualizar las probabilidades
labels = ['Nublado', 'Despejado']
probabilidades = [probabilidad_nublado_dado_mojado, 1 - probabilidad_nublado_dado_mojado]
x = np.arange(len(labels))

plt.bar(x, probabilidades, color=['blue', 'orange'])
plt.xlabel('Cielo')
plt.ylabel('Probabilidad')
plt.title('Probabilidad del cielo dado que el pasto está mojado')
plt.xticks(x, labels)
plt.show()
