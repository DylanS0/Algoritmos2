# Define la clase Commit, que representa un commit en el sistema de control de versiones
class Commit:
    # Método constructor que se llama al crear una nueva instancia de la clase
    def __init__(self, id_commit, archivos, commit_anterior=None):
        # Inicializa el atributo 'id_commit' con el valor proporcionado al crear el objeto
        self.id_commit = id_commit
        # Inicializa el atributo 'archivos' con la lista de objetos Archivo proporcionada
        self.archivos = archivos  # Lista de objetos Archivo
        # Inicializa el atributo 'commit_anterior' con el commit anterior, si se proporciona; de lo contrario, se establece en None
        self.commit_anterior = commit_anterior

    # Método especial que se llama cuando se convierte el objeto a una cadena (por ejemplo, al imprimirlo)
    def __str__(self):
        # Crea una cadena que representa todos los archivos en el commit, utilizando una comprensión de lista
        archivos_str = ', '.join(str(archivo) for archivo in self.archivos)
        # Devuelve una representación en forma de cadena del objeto, mostrando el ID del commit y los archivos asociados
        return f"Commit ID: {self.id_commit}, Archivos: [{archivos_str}]"