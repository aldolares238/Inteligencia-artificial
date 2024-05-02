#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 54/59 Análisis Léxico

import re
import matplotlib.pyplot as plt

# Definimos una cadena de texto de ejemplo
texto = "if x == 5: y = x * 2"

# Definimos patrones para identificar diferentes tipos de tokens
patrones = {
    'PALABRA_CLAVE': r'\b(if|else|for|while)\b',
    'IDENTIFICADOR': r'\b([a-zA-Z_]\w*)\b',
    'OPERADOR': r'(\+|\-|\*|\/|==|=)',
    'NUMERO': r'\b\d+\b',
    'ESPACIO': r'\s+'
}

# Inicializamos contadores para cada tipo de token
conteo_tokens = {tipo: 0 for tipo in patrones}

# Iteramos sobre cada tipo de token y contamos su ocurrencia en el texto
for tipo, patron in patrones.items():
    conteo_tokens[tipo] = len(re.findall(patron, texto))

# Visualizamos el conteo de tokens
plt.bar(conteo_tokens.keys(), conteo_tokens.values(), color='skyblue')
plt.xlabel('Tipo de Token')
plt.ylabel('Frecuencia')
plt.title('Análisis Léxico: Frecuencia de Tokens')
plt.xticks(rotation=45)
plt.show()
