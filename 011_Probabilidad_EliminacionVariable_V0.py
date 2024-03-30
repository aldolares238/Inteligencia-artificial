#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 11/60 Eliminación de Variables

# Importamos las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Creamos el modelo bayesiano
model = BayesianNetwork([('A', 'C'), ('B', 'C')])

# Definimos las distribuciones de probabilidad condicional (CPDs)
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7], [0.3]])
cpd_c = TabularCPD(variable='C', variable_card=2, 
                   values=[[0.1, 0.2, 0.5, 0.8],
                           [0.9, 0.8, 0.5, 0.2]],
                   evidence=['A', 'B'], evidence_card=[2, 2])

# Agregamos las CPDs al modelo
model.add_cpds(cpd_a, cpd_b, cpd_c)

# Verificamos la validez del modelo
assert model.check_model()

# Creamos el objeto de eliminación de variables
inference = VariableElimination(model)

# Realizamos la inferencia eliminando la variable 'A'
result = inference.query(variables=['C'], evidence={'B': 0})

# Imprimimos los resultados
print(result)

# Graficamos los resultados
labels = ['C0', 'C1']
values = [result.values[0], result.values[1]]

plt.bar(labels, values)
plt.title('Probabilidad de C dado B=0')
plt.xlabel('Valores de C')
plt.ylabel('Probabilidad')
plt.show()
