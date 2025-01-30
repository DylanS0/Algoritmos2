import datetime 
import getpass

#define la clase Commit, que representa un commit en el sistema de control de versiones (Sistema Git Simulado)
class Commit:
    #metodo constructor 
    def __init__(self, id, mensaje_commit, archivos = None,  commit_anterior=None, ):
        #inicializa el atributo id
        self.id = id
        self.mensaje_commit = mensaje_commit 
        #inicializa el atributo archivos con la lista de objetos Archivo proporcionada
        self.archivos = archivos if archivos else [] #lista de objetos Archivo
        self.mensaje_commit = mensaje_commit
        self.autor = getpass.getuser() #obtiene el nombre del autor
        self.date = datetime.datetime.now() #obtiene la fecha en la que se realiza una accion en formato ('%Y-%m-%d %H:%M:%S')
        #inicializa el atributo commit_anterior con el commit anterior, si se proporciona; de lo contrario, se establece en None
        self.commit_anterior = commit_anterior
        

    def agregar_archivo(self, archivo):
        self.archivos.append(archivo)

    
    def __str__(self):
        # Crea una cadena que representa todos los archivos en el commit, utilizando una comprension de lista
        archivos_str = ', '.join(str(archivo) for archivo in self.archivos)
        # Devuelve una representacion en forma de cadena del objeto, mostrando el ID del commit y los archivos asociados
        return f"Commit ID: {self.id}: {self.mensaje_commit} hecho por {self.autor}, Archivos: [{archivos_str}, en {self.date.strftime('%Y-%m-%d %H:%M:%S')} / commit anterior: {self.anterior}"