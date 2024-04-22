#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 26/59 Taxonomías: Categorías y Objetos

class Taxonomy:
    def __init__(self):
        # Inicializa la taxonomía como un diccionario vacío
        self.categories = {}

    def add_category(self, category, parent=None):
        # Agrega una categoría al diccionario de la taxonomía
        if category not in self.categories:
            self.categories[category] = set()  # Si la categoría no existe, crea un conjunto vacío para sus subcategorías
        if parent:  # Si se proporciona un padre, añade este a la lista de subcategorías
            if parent not in self.categories:
                self.categories[parent] = set()  # Si el padre no existe, crea un conjunto vacío para sus subcategorías
            self.categories[parent].add(category)  # Agrega la categoría como subcategoría del padre

    def get_subcategories(self, category):
        # Obtiene las subcategorías de una categoría dada
        if category in self.categories:
            return self.categories[category]  # Devuelve el conjunto de subcategorías
        else:
            return set()  # Devuelve un conjunto vacío si la categoría no tiene subcategorías

# Crear una instancia de la taxonomía para vehículos
vehiculos_taxonomy = Taxonomy()

# Agregar categorías y subcategorías de vehículos
vehiculos_taxonomy.add_category("Vehículo")
vehiculos_taxonomy.add_category("Terrestre", parent="Vehículo")
vehiculos_taxonomy.add_category("Aéreo", parent="Vehículo")
vehiculos_taxonomy.add_category("Marítimo", parent="Vehículo")
vehiculos_taxonomy.add_category("Automóvil", parent="Terrestre")
vehiculos_taxonomy.add_category("Motocicleta", parent="Terrestre")
vehiculos_taxonomy.add_category("Avión", parent="Aéreo")
vehiculos_taxonomy.add_category("Helicóptero", parent="Aéreo")
vehiculos_taxonomy.add_category("Barco", parent="Marítimo")
vehiculos_taxonomy.add_category("Yate", parent="Marítimo")

# Consultar subcategorías de vehículos
print("Subcategorías de Vehículo:", vehiculos_taxonomy.get_subcategories("Vehículo"))
print("Subcategorías de Terrestre:", vehiculos_taxonomy.get_subcategories("Terrestre"))
print("Subcategorías de Aéreo:", vehiculos_taxonomy.get_subcategories("Aéreo"))
print("Subcategorías de Marítimo:", vehiculos_taxonomy.get_subcategories("Marítimo"))
