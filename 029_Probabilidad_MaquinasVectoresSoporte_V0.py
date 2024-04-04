#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 29/60 Máquinas de Vectores Soporte (Núcleo)

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.calibration import CalibratedClassifierCV

#Cargamos el conjunto de datos de iris
iris = datasets.load_iris()
X = iris.data[:, :2]  #Tomamos solo las primeras dos características para facilitar la visualización
y = iris.target

#Dividimos el conjunto de datos en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Creamos el clasificador SVM con un núcleo (kernel) gaussiano (RBF)
svm = SVC(kernel='rbf', probability=True)

#Entrenamos el clasificador
svm.fit(X_train, y_train)

#Calibramos el clasificador para obtener probabilidades calibradas
calibrated_svm = CalibratedClassifierCV(svm, method='sigmoid', cv='prefit')

#Entrenamos el clasificador calibrado
calibrated_svm.fit(X_train, y_train)

#Visualizamos los límites de decisión
h = .02  # Tamaño del paso en la malla del gráfico
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = calibrated_svm.predict(np.c_[xx.ravel(), yy.ravel()])

#Coloreamos los puntos del gráfico según la predicción
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)

#Colocamos los puntos de entrenamiento en el gráfico
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=plt.cm.coolwarm, edgecolors='k')
plt.xlabel('Longitud del sépalo')
plt.ylabel('Anchura del sépalo')
plt.title('SVM con Núcleo (Kernel) - Clasificación Probabilística')
plt.show()

#Evaluamos el desempeño del clasificador
accuracy = calibrated_svm.score(X_test, y_test)
print("Precisión del clasificador SVM calibrado en el conjunto de prueba: {:.2f}".format(accuracy))
