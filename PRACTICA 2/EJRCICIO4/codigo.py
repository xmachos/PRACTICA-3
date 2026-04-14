class Consola:
    # Atributos
    marca = ""
    capacidad = 0.0
    juegos = []

    # 1. Constructor
    def __init__(self, marca, capacidad, juegos = None):

        self.__marca = marca
        self.__capacidad = capacidad
        self.__juegos = []

        if juegos != None:
            for j in juegos:
                self.__juegos = self.__juegos + [j]

    # 2. Elimina un juego
    def eliminarJuego(self, juego):

        nuevaLista = []

        for j in self.__juegos:
            if j != juego:
                nuevaLista = nuevaLista + [j]

        self.__juegos = nuevaLista

    # 3. Sobrecarga +
    def __add__(self, juegoNuevo):

        total = 0
        for j in self.__juegos:
            total = total + j[2]

        espacioDisponible = self.__capacidad - total

        if juegoNuevo[2] <= espacioDisponible:
            self.__juegos = self.__juegos + [juegoNuevo]

        return self

    # 4. Sobrecarga -=
    def __isub__(self, x):

        nuevaLista = []

        for j in self.__juegos:
            if j[3] != x:
                nuevaLista = nuevaLista + [j]

        self.__juegos = nuevaLista

        return self

    # 5. Sobrecarga >
    def __gt__(self, o):

        contador1 = 0
        for j in self.__juegos:
            contador1 = contador1 + 1

        contador2 = 0
        for j in o.__juegos:
            contador2 = contador2 + 1

        if contador1 > contador2:
            return self.__marca
        else:
            return o.__marca


# 🔥 PRUEBA (ESTO FALTABA)

consola = Consola("PlayStation", 16)

consola = consola + ["Plantas vs zombies", "Pop cap", 2, 'E']
consola = consola + ["Half Life", "Valve", 7, 'T']

juego = ["GTA 5", "Rock Star", 5, 'M']
consola = consola + juego

consola.eliminarJuego(juego)

consola -= 'T'
consola2 = Consola("Xbox", 64)
print(consola > consola2)