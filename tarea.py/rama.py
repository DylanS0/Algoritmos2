
#define la clase Rama, que representa una rama en el sistema de control de versiones
class Rama:
    #metodo constructor que se llama al crear una nueva instancia de la clase
    def __init__(self, nombre = 'main'):
        #inicializa el atributo 'nombre' con el valor proporcionado al crear el objeto
        self.nombre = nombre
        #inicializa el atributo 'commit_reciente' en None, indicando que no hay commits en la rama al principio
        self.commit_reciente = None
        self.lista_archivos = []    # Crea una lista para guardar los archivos que fueron añadidos a través del comando "add"
        self.lista_id = []          # Crea una lista para guardar los id de los commits
        self.lista_commits = []     # Crea una lista para guardar los commits

    
    def __str__(self):
        #devuelve una representación en forma de cadena del objeto, mostrando el nombre de la rama y el ID del commit más reciente
        return f"Rama: {self.nombre}, Commit Reciente: {self.commit_reciente.id_commit if self.commit_reciente else 'Ninguno'}"
    
    
