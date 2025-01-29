# Importa la clase Commit desde el módulo commit
from commit import Commit
# Importa la clase Rama desde el módulo rama
from rama import Rama

# Define la clase Repositorio, que representa un sistema de control de versiones
class Repositorio:
    # Método constructor que se llama al crear una nueva instancia de la clase
    def __init__(self):
        # Inicializa un diccionario para almacenar las ramas del repositorio
        self.ramas = {}
        # Inicializa el atributo 'rama_actual' en None, indicando que no hay ninguna rama activa al principio
        self.rama_actual = None

    # Método para crear una nueva rama
    def crear_rama(self, nombre):
        # Verifica si la rama con el nombre proporcionado no existe ya en el diccionario de ramas
        if nombre not in self.ramas:
            # Crea una nueva instancia de Rama y la almacena en el diccionario con el nombre como clave
            self.ramas[nombre] = Rama(nombre)
            # Si no hay ninguna rama activa, establece la nueva rama como la rama actual
            if self.rama_actual is None:
                self.rama_actual = self.ramas[nombre]
            # Imprime un mensaje indicando que la rama ha sido creada
            print(f"Rama '{nombre}' creada.")
        else:
            # Si la rama ya existe, imprime un mensaje indicando que no se puede crear
            print(f"La rama '{nombre}' ya existe.")

    # Método para realizar un commit en la rama actual
    def realizar_commit(self, archivos):
        # Verifica si hay una rama activa
        if self.rama_actual is None:
            print("No hay ninguna rama activa.")
            return  # Sale del método si no hay rama activa

        # Calcula el ID del nuevo commit
        id_commit = len(self.rama_actual.archivos) + 1 if self.rama_actual.commit_reciente is None else self.rama_actual.commit_reciente.id_commit + 1
        # Crea una nueva instancia de Commit con el ID, los archivos y el commit anterior
        nuevo_commit = Commit(id_commit, archivos, self.rama_actual.commit_reciente)
        # Actualiza el commit más reciente de la rama actual con el nuevo commit
        self.rama_actual.commit_reciente = nuevo_commit
        # Imprime un mensaje indicando que el commit ha sido realizado
        print(f"Commit realizado: {nuevo_commit}")

    # Método para cambiar la rama activa
    def cambiar_rama(self, nombre):
        # Verifica si la rama con el nombre proporcionado existe en el diccionario de ramas
        if nombre in self.ramas:
            # Establece la rama actual como la rama con el nombre proporcionado
            self.rama_actual = self.ramas[nombre]
            # Imprime un mensaje indicando que se ha cambiado a la nueva rama
            print(f"Cambiado a la rama '{nombre}'.")
        else:
            # Si la rama no existe, imprime un mensaje indicando que no se puede cambiar
            print(f"La rama '{nombre}' no existe.")

    # Método para fusionar una rama en la rama actual
    def fusionar_rama(self, nombre):
        # Verifica si la rama con el nombre proporcionado existe en el diccionario de ramas
        if nombre in self.ramas:
            # Obtiene la rama que se desea fusionar
            rama_a_fusionar = self.ramas[nombre]
            # Verifica si la rama a fusionar tiene un commit reciente
            if rama_a_fusionar.commit_reciente:
                # Realiza un commit en la rama actual con los archivos del commit más reciente de la rama a fusionar
                self.realizar_commit(rama_a_fusionar.commit_reciente.archivos)
                # Imprime un mensaje indicando que la fusión ha sido realizada
                print(f"Rama '{nombre}' fusionada en '{self.rama_actual.nombre}'.")
            else:
                # Si la rama a fusionar no tiene commits, imprime un mensaje indicando que no se puede fusionar
                print(f"La rama '{nombre}' no tiene commits para fusionar.")
        else:
            # Si la rama no existe, imprime un mensaje indicando que no se puede fusionar
            print(f"La rama '{nombre}' no existe.")