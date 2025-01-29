# Importa la clase Archivo desde el módulo archivo
from archivo import Archivo
# Importa la clase Repositorio desde el módulo repositorio
from repositorio import Repositorio

# Define la función principal del programa
def main():
    # Crea una instancia de la clase Repositorio, que representa el sistema de control de versiones
    repo = Repositorio()

    # Crear ramas
    # Llama al método crear_rama de la instancia repo para crear una rama llamada "main"
    repo.crear_rama("main")
    # Llama al método crear_rama de la instancia repo para crear una rama llamada "desarrollo"
    repo.crear_rama("desarrollo")

    # Cambiar a la rama principal y realizar un commit
    # Cambia la rama activa a "main" utilizando el método cambiar_rama
    repo.cambiar_rama("main")
    # Crea una instancia de la clase Archivo con el nombre "archivo1.txt" y un contenido específico
    archivo1 = Archivo("archivo1.txt", "Contenido del archivo 1")
    # Realiza un commit en la rama actual (main) con el archivo creado, pasando una lista con el archivo
    repo.realizar_commit([archivo1])

    # Cambiar a la rama de desarrollo y realizar un commit
    # Cambia la rama activa a "desarrollo" utilizando el método cambiar_rama
    repo.cambiar_rama("desarrollo")
    # Crea una instancia de la clase Archivo con el nombre "archivo2.txt" y un contenido específico
    archivo2 = Archivo("archivo2.txt", "Contenido del archivo 2")
    # Realiza un commit en la rama actual (desarrollo) con el archivo creado, pasando una lista con el archivo
    repo.realizar_commit([archivo2])

    # Volver a la rama principal y fusionar la rama de desarrollo
    # Cambia la rama activa de nuevo a "main" utilizando el método cambiar_rama
    repo.cambiar_rama("main")
    # Llama al método fusionar_rama para fusionar los cambios de la rama "desarrollo" en la rama actual (main)
    repo.fusionar_rama("desarrollo")

# Este bloque se ejecuta solo si el script se ejecuta directamente (no si se importa como módulo)
if __name__ == "__main__":
    # Llama a la función main para iniciar la ejecución del programa
    main()