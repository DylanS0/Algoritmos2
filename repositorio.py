from commit import Commit
from rama import Rama
import random

#define la clase Repositorio, que representa un sistema de control de versiones (Sistema Git Simulado)
class Repositorio:
    def __init__(self):
        self.ramas = Rama("nombre_de_la_rama")
        self.rama_actual = self.ramas 
        self.lista_ramas = [self.ramas]  # Lista de ramas

    # Método para crear una nueva rama
    def crear_rama(self, nombre):
        # Verifica si la rama con el nombre proporcionado no existe ya en la lista de ramas
        if nombre not in self.ramas:
            self.ramas[nombre] = Rama(nombre)
            # Si no hay ninguna rama activa, establece la nueva rama como la rama actual
            if self.rama_actual is None:
                self.rama_actual = self.ramas[nombre]
            # Imprime un mensaje indicando que la rama ha sido creada
            print(f"Rama '{nombre}' creada.")
        else:
            # Si la rama ya existe, imprime un mensaje indicando que no se puede crear
            print(f"La rama '{nombre}' ya existe.")

    #metodo para realizar un commit en la rama actual
    def realizar_commit(self, archivos):
        #verifica si hay una rama activa
        if self.rama_actual is None:
            print("No hay ninguna rama activa.")
            return  #sale del método si no hay rama activa

        #Calcula el id del nuevo commit
        while True:
            commit_id = str(random.randir(10000,99999))

            if commit_id not in self.rama_actual.lista_id:
                self.rama_actual.lista_id.append(commit_id)
                break

        nuevo_commit = Commit(commit_id, archivos, self.rama_actual.commit_reciente)
        #actualiza el commit más reciente de la rama actual con el nuevo commit
        self.rama_actual.commit_reciente = nuevo_commit
        #imprime un mensaje indicando que el commit ha sido realizado
        print(f"Commit realizado: {nuevo_commit}")

    #metodo para cambiar la rama activa
    def cambiar_rama(self, nombre):
        #verifica si la rama con el nombre proporcionado existe en la lista de ramas
        if nombre in self.ramas:
            #establece la rama actual como la rama con el nombre proporcionado
            self.rama_actual = self.ramas[nombre]
            #imprime un mensaje indicando que se ha cambiado a la nueva rama
            print(f"Cambiado a la rama '{nombre}'.")
        else:
            #si la rama no existe, imprime un mensaje indicando que no se puede cambiar
            print(f"La rama '{nombre}' no existe.")

    # mrtodo para fusionar una rama en la rama actual
    def fusionar_rama(self, nombre):
        #verifica si la rama con el nombre proporcionado existe en la lista de ramas
        if nombre in self.ramas:
            #obtiene la rama que se desea fusionar
            rama_a_fusionar = self.ramas[nombre]
            #verifica si la rama a fusionar tiene un commit reciente
            if rama_a_fusionar.commit_reciente:
                self.realizar_commit(rama_a_fusionar.commit_reciente.archivos)
                print(f"Rama '{nombre}' fusionada en '{self.rama_actual.nombre}'.")
            else:
                # Si la rama a fusionar no tiene commits, imprime un mensaje indicando que no se puede fusionar
                print(f"La rama '{nombre}' no tiene commits para fusionar.")
        else:
            # Si la rama no existe, imprime un mensaje indicando que no se puede fusionar
            print(f"La rama '{nombre}' no existe.")
            
    def mostrar_ramas(self):
        for i, r in enumerate(self.ramas):
            print(f"{r.nombre_rama}")
