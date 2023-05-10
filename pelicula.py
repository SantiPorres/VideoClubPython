class Pelicula:
    def __init__(self, codigo, titulo, genero):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.alquilada = False
        self.socio = ""

    def mostrar_pelicula(self):
        print("Código: ", self.codigo)
        print("Titulo: ", self.titulo)
        print("Genero: ", self.genero)
        if self.alquilada == False:
            print("Estado: Disponible")
        else:
            print("Estado: Alquilada")

    def mostrar_pelicula_disponible(self):
        if self.alquilada == False:
            print("Código: ", self.codigo)
            print("Titulo: ", self.titulo)
            print("Genero: ", self.genero)

    def mostrar_pelicula_alquilada(self):
        if self.alquilada == True:
            print("Código: ", self.codigo)
            print("Titulo: ", self.titulo)
            print("Genero: ", self.genero)
            print("Código del socio: ", self.socio)
