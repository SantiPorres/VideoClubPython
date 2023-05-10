class Socio:

    def __init__(self, codigo, nombre, telefono, direccion, titulo_pelicula, peliculas_alquiladas):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.titulo_pelicula = titulo_pelicula
        self.peliculas_alquiladas = peliculas_alquiladas

    def mostrar_socio(self):
        print("Código: " + self.codigo)
        print("Nombre: " + self.nombre)
        print("Telefono: " + self.telefono)
        print("Dirección: " + self.direccion)
        if self.peliculas_alquiladas != 0:
            #print("Número de peliculas alquiladas: " + str(self.peliculas_alquiladas))
            print("Pelicula alquilada: " + self.titulo_pelicula)