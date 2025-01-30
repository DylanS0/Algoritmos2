# Define la clase Archivo, que representa un archivo en el sistema de control de versiones (Sistema Git Simulado)
class Archivo:
    # Método constructor 
    def __init__(self, nombre, contenido):
        # Inicializa el atributo 'nombre' 
        self.nombre = nombre
        # Inicializa el atributo 'contenido' 
        self.contenido = contenido

    # Método especial que se llama cuando se convierte el objeto a una cadena (por ejemplo, al imprimirlo)
    def __str__(self):
        # Devuelve una representación en forma de cadena del objeto, mostrando el nombre y el contenido del archivo
        return f"Archivo: {self.nombre}, Contenido: {self.contenido}"
