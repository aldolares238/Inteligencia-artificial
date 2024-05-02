#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 44/59 Árboles de Decisión: ID3

import numpy as np
import matplotlib.pyplot as plt

# Definimos una función para calcular la entropía de un conjunto de datos
def entropy(y):
    classes, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

# Definimos una función para calcular la ganancia de información
def information_gain(X, y, feature_index):
    # Calculamos la entropía del conjunto original
    original_entropy = entropy(y)
    
    # Dividimos el conjunto en función del valor del atributo en feature_index
    values, counts = np.unique(X[:, feature_index], return_counts=True)
    weighted_entropy = 0
    
    # Calculamos la entropía ponderada de cada subconjunto
    for value, count in zip(values, counts):
        subset_indices = np.where(X[:, feature_index] == value)[0]
        subset_entropy = entropy(y[subset_indices])
        weighted_entropy += (count / len(y)) * subset_entropy
    
    # Calculamos la ganancia de información
    information_gain = original_entropy - weighted_entropy
    return information_gain

# Implementamos la clase Node para representar un nodo en el árbol de decisión
class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

# Implementamos la clase DecisionTreeID3 para el algoritmo ID3
class DecisionTreeID3:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
    
    # Método para entrenar el árbol de decisión
    def fit(self, X, y):
        self.root = self._grow_tree(X, y)
    
    # Método privado para construir el árbol de decisión recursivamente
    def _grow_tree(self, X, y, depth=0):
        # Verificamos si se alcanzó la profundidad máxima o si todos los datos tienen la misma etiqueta
        if depth == self.max_depth or len(np.unique(y)) == 1:
            return Node(value=np.argmax(np.bincount(y)))
        
        n_features = X.shape[1]
        best_feature = None
        best_threshold = None
        best_gain = -np.inf
        
        # Iteramos sobre cada atributo para encontrar el mejor atributo y umbral para dividir
        for feature_index in range(n_features):
            thresholds = np.unique(X[:, feature_index])
            for threshold in thresholds:
                # Dividimos los datos en función del atributo y umbral actual
                left_indices = np.where(X[:, feature_index] <= threshold)[0]
                right_indices = np.where(X[:, feature_index] > threshold)[0]
                
                # Calculamos la ganancia de información
                gain = information_gain(X, y, feature_index)
                
                # Actualizamos el mejor atributo y umbral si encontramos una mejor ganancia de información
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature_index
                    best_threshold = threshold
        
        # Si no se puede encontrar una mejor división, devolvemos un nodo hoja con la clase mayoritaria
        if best_gain == 0:
            return Node(value=np.argmax(np.bincount(y)))
        
        # Dividimos los datos en función del mejor atributo y umbral encontrado
        left_indices = np.where(X[:, best_feature] <= best_threshold)[0]
        right_indices = np.where(X[:, best_feature] > best_threshold)[0]
        left_subtree = self._grow_tree(X[left_indices], y[left_indices], depth + 1)
        right_subtree = self._grow_tree(X[right_indices], y[right_indices], depth + 1)
        
        # Creamos y devolvemos un nodo de decisión
        return Node(feature=best_feature, threshold=best_threshold, left=left_subtree, right=right_subtree)
    
    # Método para predecir la clase de un conjunto de datos
    def predict(self, X):
        return np.array([self._predict_tree(x, self.root) for x in X])
    
    # Método privado para predecir la clase de una instancia utilizando el árbol de decisión
    def _predict_tree(self, x, node):
        if node.value is not None:
            return node.value
        if x[node.feature] <= node.threshold:
            return self._predict_tree(x, node.left)
        else:
            return self._predict_tree(x, node.right)

# Creamos un conjunto de datos de ejemplo
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([0, 1, 1, 0])

# Creamos y entrenamos el árbol de decisión
tree = DecisionTreeID3(max_depth=2)
tree.fit(X, y)

# Realizamos predicciones sobre el mismo conjunto de datos para visualizar el árbol
predictions = tree.predict(X)

# Visualizamos el árbol de decisión
def plot_tree(node, depth=0):
    if node.value is not None:
        plt.text(depth, 0.5, f'Clase: {node.value}', va='center', ha='center')
    else:
        plt.text(depth, 0.5, f'Atributo: {node.feature}\nUmbral: {node.threshold}', va='center', ha='center')
        plt.plot([depth, depth-1], [0.4, 0.2], '-k')  # Línea hacia el nodo izquierdo
        plt.plot([depth, depth-1], [0.6, 0.8], '-k')  # Línea hacia el nodo derecho
        plot_tree(node.left, depth - 1)
        plot_tree(node.right, depth - 1)

plt.figure(figsize=(8, 4))
plt.title('Árbol de Decisión ID3')
plt.axis('off')
plot_tree(tree.root)
plt.show()
