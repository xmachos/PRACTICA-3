#No sabia de que enviar
class Aula:
    def __init__(self, nombreAula, piso):
        self.nombreAula = nombreAula
        self.piso = piso
        self.estudiantes = []

    def agregarEstudiante(self, nombre, nota):
        self.estudiantes.append([nombre, nota])

    def mostrarDatos(self):
        print(self.nombreAula, self.piso)
        for e in self.estudiantes:
            print(e[0], e[1])

    def mostrarEstado(self):
        for e in self.estudiantes:
            if e[1] >= 51:
                print(e[0], e[1], "APEROBADO")
            else:
                print(e[0], e[1], "REPROBADO")



a = Aula("Aula 101", 1)
a.agregarEstudiante("Luis", 67)
a.agregarEstudiante("Aracely", 89)
a.mostrarDatos()
a.mostrarEstado()