from os import system

class VideoClub:

    def __init__(self):
        self.socios = []
        self.peliculas = []

    def buscar_socio(self, codigo):
        for i in range(len(self.socios)):
            if self.socios[i].codigo == codigo:
                return i
        return -1

    def adicionar_socio(self, socio):
        if self.buscar_socio(socio.codigo) == -1:
            self.socios.append(socio)
            return True
        return False

    def listar_pelicula(self):
        for pelicula in self.peliculas:
            print("************************")
            pelicula.mostrar_pelicula()

    def modificar_pelicula(self, codigo):
        pos_pelicula = self.buscar_pelicula(codigo)
        if pos_pelicula != -1:
            if self.peliculas[pos_pelicula].codigo == codigo:
                print("************************")
                print(" OPCIONES PARA MODIFICAR ")
                print("************************")

                try:
                    print("1: Modificar el título")
                    print("2: Modificar el genero")
                    print("************************")
                    opcion = int(input("Digite la opción a modificar: "))

                    if opcion == 1:
                        titulo = input("Digite el nuevo título: ")
                        self.peliculas[pos_pelicula].titulo = titulo
                        return True
                    
                    elif opcion == 2:
                        genero = input("Digite el nuevo genero: ")
                        self.peliculas[pos_pelicula].genero = genero
                        return True
                
                    else:
                        return False
                    
                except ValueError:
                    print("************************")
                    print("Error - El dato debe ser entero")
                    print("************************")
                    input()
            else:
                return False
        else:
            return False
        
    def eliminar_pelicula(self, codigo):
        pos = self.buscar_pelicula(codigo)
        if pos != -1:
            del(self.peliculas[pos])
            return True
        return False

    def listar_socios(self):
        for socio in self.socios:
        #for socio in range(len(self.socios)):
            socio.mostrar_socio()
            print("************************")
            #print(self.socios[socio])

    def modificar_socio(self, codigo):
        pos_socio = self.buscar_socio(codigo)

        if pos_socio != -1:
            if self.socios[pos_socio].codigo == codigo:
                system("clear")
                print("************************")
                print("OPCIONES DE MODIFICACIÓN")
                print("************************")
                try:
                    print("1: Modificar el nombre del socio")
                    print("2: Modificar el telefono del socio")
                    print("3: Modificar la dirección del socio")
                    print("***********************************")

                    opcion = int(input("Seleccione la opción: "))

                    if opcion == 1:
                        nombre = input("Ingrese el nuevo nombre del socio: ")
                        self.socios[pos_socio].nombre = nombre
                        return True
                    elif opcion == 2:
                        telefono = input("Ingrese el nuevo telefono del socio: ")
                        self.socios[pos_socio].telefono = telefono
                        return True
                    elif opcion == 3:
                        direccion = input("Ingrese la nueva dirección del socio: ")
                        self.socios[pos_socio].direccion = direccion
                        return True
                    else: 
                        return False
                except ValueError:
                    print("************************")
                    print("Error - el dato ingresado debe ser entero")
                    print("************************")
            else:
                return False
        else:
            return False
        
    
    def eliminar_socio(self, codigo):
        pos_socio = self.buscar_socio(codigo)

        if pos_socio != -1:
            del(self.socios[pos_socio])
            return True
        return False

    def buscar_pelicula(self, codigo):
        for i in range(len(self.peliculas)):
            if self.peliculas[i].codigo == codigo:
                return i
        return -1
    
    def adicionar_pelicula(self, pelicula):
        if self.buscar_pelicula(pelicula.codigo) == -1:
            self.peliculas.append(pelicula)
            return True
        return False
                    
