from socio import Socio
from videoclub import VideoClub
from os import system
from pelicula import Pelicula

class Menu:
    def __init__(self):
        self.videoclub = VideoClub()


    def crear_socio(self):
        system("clear")
        print("************************")
        print("****** CREAR SOCIO *****")
        print("************************")

        codigo = input("Ingrese el código del socio: ")
        nombre = input("Ingrese el nombre del socio: ")
        telefono = input("Ingrese el telefono del socio: ")
        direccion = input("Ingrese la dirección del socio: ")

        socio = Socio(codigo, nombre, telefono, direccion)

        if self.videoclub.adicionar_socio(socio):
            print("************************")
            print("Info - El socio fue creado correctamente")
            print("************************")
            input("Enter para continuar")

        else:
            print("************************")
            print("Error - El socio no fue adicionado")
            print("************************")
            input("Enter para continuar")
    

    def listar_socios(self):
        system("clear")
        print("************************")
        print("**** LISTAR SOCIOS *****")
        print("************************")
        self.videoclub.listar_socios()
        input("Enter para continuar")


    def modificar_socio(self):
        system("clear")
        print("************************")
        print("*** MODIFICAR SOCIO ***")
        print("************************")
        codigo = input("Ingrese el código del socio que desea modificar: ")

        if self.videoclub.modificar_socio(codigo):
            system("clear")
            print("************************")
            print("Info - El socio fue modificado correctamente")
            print("************************")
            input("Enter para continuar")
        else:
            system("clear")
            print("************************")
            print("Info - El socio no fue modificado")
            print("************************")
            input("Enter para continuar")


    def eliminar_socio(self):
        system("clear")
        print("************************")
        print("*** ELIMINAR SOCIO ***")
        print("************************")
        codigo = input("Ingrese el código del socio que desea eliminar: ")

        if self.videoclub.eliminar_socio(codigo):
            system("clear")
            print("************************")
            print("Info - El socio fue eliminado correctamente")
            print("************************")
            input("Enter para continuar")
        else:
            system("clear")
            print("************************")
            print("Info - El socio no fue eliminado")
            print("************************")
            input("Enter para continuar")


    def crear_pelicula(self):
        system("clear")
        print("************************")
        print("**** CREAR PELICULA ****")
        print("************************")
        codigo = input("Digite el código de la pelicula: ")
        titulo = input("Digite el titulo de la pelicula: ")
        genero = input("Digite el genero de la pelicula: ")
        pelicula = Pelicula(codigo, titulo, genero)

        if self.videoclub.adicionar_pelicula(pelicula):
            system("clear")
            print("************************")
            print("Info - La pelicula fue almacenada correctamente")
            print("************************")
            input("Enter para continuar")
        else:
            system("clear")
            print("************************")
            print("Info - La pelicula ya existe")
            print("************************")
            input("Enter para continuar")

        
    def listar_peliculas(self):
        system("clear")
        print("************************")
        print("*** LISTAR PELICULA ****")
        print("************************")
        self.videoclub.listar_pelicula()
        input("Enter para continuar")

    
    def modificar_pelicula(self):
        system("clear")
        print("************************")
        print("** MODIFICAR PELICULA **")
        print("************************")
        codigo = input("Digite el código de la pelicula: ")

        if self.videoclub.modificar_pelicula(codigo):
            print("************************")
            print("Info - La pelicula fue modificada correctamente")
            print("************************")
            input("Enter para continuar")
        else:
            print("************************")
            print("Info - La pelicula no se pudo modificar")
            print("************************")
            input("Enter para continuar")


    def eliminar_pelicula(self):
        system("clear")
        print("************************")
        print("** ELIMINAR PELICULA **")
        print("************************")
        codigo = input("Digite el código de la pelicula: ")

        if self.videoclub.eliminar_pelicula(codigo):
            print("************************")
            print("Info - La pelicula fue eliminada correctamente")
            print("************************")
            input("Enter para continuar")
        else:
            print("************************")
            print("Info - La pelicula no se pudo eliminar")
            print("************************")
            input("Enter para continuar")


    def mostrar_menu_principal(self):
        while(True):
            system("clear")
            print("************************")
            print("****** VIDEOCLUB *******")
            print("************************")
            print("**** Menu Principal ****")
            print("************************")
            print("1: Crear socio")
            print("2: Listar socios")
            print("3: Modificar socio")
            print("4: Eliminar socio")
            print("5: Crear pelicula")
            print("6: Listar peliculas")
            print("7: Modificar pelicula")
            print("8: Eliminar pelicula")
            print("0: Salir")
            print("************************")
            
            try:
                opcion = int(input("Seleccione la opción: "))

                if opcion == 1:
                    self.crear_socio()
                elif opcion == 2:
                    self.listar_socios()
                elif opcion == 3:
                    self.modificar_socio()
                elif opcion == 4:
                    self.eliminar_socio()
                elif opcion == 5:
                    self.crear_pelicula()
                elif opcion == 6:
                    self.listar_peliculas()
                elif opcion == 7:
                    self.modificar_pelicula()
                elif opcion == 8:
                    self.eliminar_pelicula()
                elif opcion == 0:
                    break
                else:
                    print("************************")
                    print("Error - Opción Invalida")
                    print("************************")
                    input()
            except ValueError:
                print("************************")
                print("Error - el dato ingresado debe ser entero")
                print("************************")
                input("Enter para continuar")


if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu_principal()
                    
