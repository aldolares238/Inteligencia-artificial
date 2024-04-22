#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 10/59 Reglas de Diagnóstico y Causales

# Importamos las bibliotecas necesarias
import matplotlib.pyplot as plt

# Definimos las reglas de diagnóstico y causales
# En este ejemplo, utilizaremos reglas simples para demostración
def diagnostic_rules(symptoms):
    diagnosis = "Indefinido"
    if 'fiebre' in symptoms and 'tos' in symptoms:
        diagnosis = "Gripe"
    elif 'dolor_de_cabeza' in symptoms and 'fiebre' not in symptoms:
        diagnosis = "Migraña"
    return diagnosis

# Definimos los síntomas del paciente
patient_symptoms = ['fiebre', 'tos']

# Realizamos el diagnóstico utilizando las reglas
diagnosis_result = diagnostic_rules(patient_symptoms)

# Mostramos el resultado del diagnóstico
print("Diagnóstico:", diagnosis_result)

# Creamos una representación gráfica del diagnóstico
# Esto solo es un ejemplo básico de visualización
labels = ['Gripe', 'Migraña', 'Indefinido']
sizes = [patient_symptoms.count('fiebre') + patient_symptoms.count('tos'), 
         patient_symptoms.count('dolor_de_cabeza'), 
         len(patient_symptoms) - patient_symptoms.count('fiebre') - patient_symptoms.count('tos') - patient_symptoms.count('dolor_de_cabeza')]
colors = ['lightcoral', 'lightskyblue', 'lightgreen']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Diagnóstico de los síntomas')
plt.show()
