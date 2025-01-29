# Define la clase Rama, que representa una rama en el sistema de control de versiones
class Rama:
    # Método constructor que se llama al crear una nueva instancia de la clase
    def __init__(self, nombre):
        # Inicializa el atributo 'nombre' con el valor proporcionado al crear el objeto
        self.nombre = nombre
        # Inicializa el atributo 'commit_reciente' en None, indicando que no hay commits en la rama al principio
        self.commit_reciente = None

    # Método especial que se llama cuando se convierte el objeto a una cadena (por ejemplo, al imprimirlo)
    def __str__(self):
        # Devuelve una representación en forma de cadena del objeto, mostrando el nombre de la rama y el ID del commit más reciente
        return f"Rama: {self.nombre}, Commit Reciente: {self.commit_reciente.id_commit if self.commit_reciente else 'Ninguno'}"