from commit import Commit
from random import randint

#define la clase Archivo, que representa un archivo en el sistema de control de versiones (Sistema Git Simulado)
class Archivo:
    #metodo constructor 
    def __init__(self, nombre, contenido):
        #inicializa el atributo 'nombre' 
        self.nombre = nombre
        #inicializa el atributo 'contenido' 
        self.contenido = contenido

    
    def __str__(self):
        #muestra el nombre y el contenido del archivo
        return f"Archivo: {self.nombre}, Contenido: {self.contenido}"
