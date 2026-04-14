class Persona:
    def __init__(self, nombre, carnet, edad):
        self.nombre = nombre
        self.carnet = carnet
        self.edad = edad
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Carnet:", self.carnet)
        print("Edad:", self.edad)
class Estudiante(Persona):
    def __init__(self, nombre, carnet, edad, matricula, carrera):
        super().__init__(nombre, carnet, edad)
        self.matricula = matricula
        self.carrera = carrera
    def mostrar(self):
        super().mostrar()
        print("Matrícula:", self.matricula)
        print("Carrera:", self.carrera)
class Docente(Persona):
    def __init__(self, nombre, carnet, edad, antiguedad, sueldo):
        super().__init__(nombre, carnet, edad)
        self.antiguedad = antiguedad
        self.sueldo = sueldo
    def mostrar(self):
        super().mostrar()
        print("Antigüedad:", self.antiguedad)
        print("Sueldo:", self.sueldo)
est1 = Estudiante("Juan", 123, 20, 1001, "Sistemas")
est2 = Estudiante("Maria", 456, 25, 1002, "Sistemas")
doc = Docente("Carlos", 789, 25, 10, 5000)
print("----- ESTUDIANTE 1 -----")
est1.mostrar()
print("\n----- ESTUDIANTE 2 -----")
est2.mostrar()
print("\n----- DOCENTE -----")
doc.mostrar()
if est1.edad == doc.edad or est2.edad == doc.edad:
    print("\nAlgún estudiante tiene la misma edad que el docente")
else:
    print("\nNingún estudiante tiene la misma edad que el docente")
def misma_carrera(e1, e2):
    if e1.carrera == e2.carrera:
        return True
    else:
        return False


if misma_carrera(est1, est2):
    print("Los estudiantes están en la misma carrera")
else:
    print("Los estudiantes NO están en la misma carrera")