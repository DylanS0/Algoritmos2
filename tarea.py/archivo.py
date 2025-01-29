# Define la clase Archivo, que representa un archivo en el sistema de control de versiones
class Archivo:
    # Método constructor que se llama al crear una nueva instancia de la clase
    def __init__(self, nombre, contenido):
        # Inicializa el atributo 'nombre' con el valor proporcionado al crear el objeto
        self.nombre = nombre
        # Inicializa el atributo 'contenido' con el valor proporcionado al crear el objeto
        self.contenido = contenido

    # Método especial que se llama cuando se convierte el objeto a una cadena (por ejemplo, al imprimirlo)
    def __str__(self):
        # Devuelve una representación en forma de cadena del objeto, mostrando el nombre y el contenido del archivo
        return f"Archivo: {self.nombre}, Contenido: {self.contenido}"