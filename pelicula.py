class Pelicula:
    def __init__(self, codigo, titulo, genero):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.alquilada = False

    def mostrar_pelicula(self):
        print("Código: ", self.codigo)
        print("Titulo: ", self.titulo)
        print("Genero: ", self.genero)
        if self.alquilada == False:
            print("Estado: Disponible")
        else:
            print("Estado: Alquilada")
