#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 7/60 Red Bayesiana

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator

#Creamos un conjunto de datos de ejemplo
data = np.random.randint(low=0, high=2, size=(1000, 2))
data[:, 1] = data[:, 0] ^ 1  #Segunda columna es la negación de la primera

#Creamos el modelo de la red bayesiana
model = BayesianModel([('A', 'B')])

#Aprendemos los parametros del modelo usando Maximum Likelihood Estimator
mle = MaximumLikelihoodEstimator(model, data)
model.fit(data, estimator=mle)

#Dibujamos el modelo
plt.figure(figsize=(8, 6))
nx.draw(model, with_labels=True, node_color='skyblue', node_size=2000, font_size=20, arrowsize=20)
plt.title("Red Bayesiana Simple")
plt.show()

#Realizamos una inferencia simple (obtenemos la probabilidad de A dado B)
inference = model.predict_proba(variables=['A'], evidence={'B': 1})
print("Probabilidad de A dado B=1:", inference[0].values[1])
