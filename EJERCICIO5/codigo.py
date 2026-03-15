class Bus:

    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.dinero = 0
    def subir_pasajeros(self, x):
        if self.pasajeros + x <= self.capacidad:
            self.pasajeros = self.pasajeros + x
            print("Subieron", x, "pasajeros")
        else:
            print("No hay suficientes asientos")
    def cobrar_pasaje(self):
        costo = 1.50
        total = self.pasajeros * costo
        self.dinero = self.dinero + total
        print("Dinero cobado:", total)
    def asientos_disponibles(self):
        disponibles = self.capacidad - self.pasajeros
        print("Asientos dsponibles:", disponibles)
bus1 = Bus(40)
bus1.subir_pasajeros(10)
bus1.cobrar_pasaje()
bus1.asientos_disponibles()