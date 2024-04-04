#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 30/60 Aprendizaje Profundo (Deep Learning)

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#Creamos un conjunto de datos de ejemplo para nuestro procedimiento
np.random.seed(0)
X = np.random.rand(100, 1)
y = 2 * X + 1 + np.random.randn(100, 1) * 0.1

#Definimos el modelo de red neuronal que vamos a utilizar en el ejemplo
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),  #Creamos Capa de entrada con forma (1,)
    tf.keras.layers.Dense(units=1)  #Creamos Capa densa con una sola neurona
])

#Compilamos el modelo
model.compile(optimizer='adam', loss='mse')  # Optimizador Adam y función de pérdida de error cuadrático medio

#Entrenamos el modelo
history = model.fit(X, y, epochs=50, verbose=0)  # Entrenamos durante 50 épocas

#Evaluamos el modelo
loss = model.evaluate(X, y)

#Mostramos la pérdida final
print("Pérdida final:", loss)

#Visualizamos el proceso de entrenamiento
plt.plot(history.history['loss'])
plt.title('Proceso de Entrenamiento')
plt.xlabel('Época')
plt.ylabel('Pérdida')
plt.show()

#Generamos predicciones con el modelo entrenado
X_test = np.linspace(0, 1, 100).reshape(-1, 1)
y_pred = model.predict(X_test)

#Visualizamos las predicciones
plt.scatter(X, y, label='Datos de entrenamiento')
plt.plot(X_test, y_pred, color='red', label='Predicciones')
plt.title('Predicciones del Modelo')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

