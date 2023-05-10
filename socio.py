class Socio:

    def __init__(self, codigo, nombre, telefono, direccion):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def mostrar_socio(self):
        print("Código: " + self.codigo)
        print("Nombre: " + self.nombre)
        print("Telefono: " + self.telefono)
        print("Dirección: " + self.direccion)