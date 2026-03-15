class Videojego:
    def __init__(self, nombre, plataforma, cantidadJugadores=0):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidadJugadores = cantidadJugadores
    def agregarJugador(self):
        self.cantidadJugadores = self.cantidadJugadores + 1
    def agregarJugadores(self, cantidad):
        self.cantidadJugadores = self.cantidadJugadores + cantidad



v1 = Videojego("FIFA", "PC")
v2 = Videojego("minecraft", "xbox", 5)
v1.agregarJugador()
cantidad = int(input())
v2.agregarJugadores(cantidad)
print(v1.nombre, v1.plataforma, v1.cantidadJugadores)
print(v2.nombre, v2.plataforma, v2.cantidadJugadores)