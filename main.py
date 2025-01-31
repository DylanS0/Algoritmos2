from archivo import Archivo
from repositorio import Repositorio
from commit import Commit 
# Define la función principal main
def main():
    repo = Repositorio()
    print("Repositorios")
    repo.crear_rama()
    repo.crear_rama()
    repo.cambiar_rama()
    #repo.crear_rama("main")
    #repo.crear_rama("desarrollo")
    #repo.cambiar_rama("main")"
    
    
    while True:
        #menu
        print("Agregar archivo = 1")
        print("Realizar un commit = 2")
        print("Crear rama = 3")
        print("Cambiar rama = 4")
        print("Mostrar ramas = 5")
        print("Fusionar rama: 6")
        print("Terminar = 0")
        
        accion = int(input(f"Seleccione un número para continuar ({repo.ramas[repo.index].nombre_rama}): "))


            
        match accion:
                case 1:
                    nombre = input("Nombre del archivo: ")
                    contenido = input("contenido del archivo: ")
                    repo.agregar_archivo(nombre, contenido)
                    pass
                
                case 2: 
                    mensaje = input("Mensaje del commit: ")
                    repo.realizar_commit(mensaje)
                    

                case 3:
                    
                    nombre_rama = input("Nombre de la rama: ")
                    repo.crear_rama(nombre_rama)
                    print(f"La rama se creó")
                        
                        
                case 4:
                    nombre_rama = input("Nombre de la rama a la que desea cambiar: ")
                    
                    if repo.cambiar_rama(nombre_rama):
                        print(f"Cambiado a la rama '{nombre_rama}'.")
                    else:
                        print(f"La rama '{nombre_rama}' no existe.")
                    
                case 5: 
                    repo.mostrar_ramas()
                
                case 6:
                    rama_a_fusionar = input("Nombre de la rama a fusionar: ")
                    if repo.fusionar_rama(rama_a_fusionar):
                        print(f"La rama '{rama_a_fusionar}' se ha fusionado con la rama actual.")
                    else:
                        print(f"No se pudo fusionar la rama '{rama_a_fusionar}'.")
                    
                        
                case 0: 
                    print("Programa finalizado")
                    
                    
                case _:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")
        
                    break
main()
    