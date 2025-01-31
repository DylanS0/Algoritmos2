
#define la clase Rama, que representa una rama en el sistema de control de versiones
class Rama:
    #metodo constructor que se llama al crear una nueva instancia de la clase
    def __init__(self, nombre_rama, commit_reciente = None):
        #inicializa el atributo nombre_rama
        self.nombre_rama = nombre_rama
        #inicializa el atributo commit_reciente en None, indicando que no hay commits en la rama al principio
        
        self.lista_archivos = []    #crea una lista para guardar los archivos 
        self.lista_id = []          #crea una lista para guardar los id de los commits
        self.lista_commits = []     #crea una lista para guardar los commits

    
    def __str__(self):
        #devuelve una representación en forma de cadena del objeto, mostrando el nombre_rama de la rama y el ID del commit más reciente
        return f"Rama: {self.nombre_rama}, Commit Reciente: {self.commit_reciente.id_commit if self.commit_reciente else 'Ninguno'}"
    
    
