class SueldoInvalidoException(Exception):
    pass


class CargoInvalidoException(Exception):
    pass


class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo

    def __str__(self):
        return f"Nombre: {self.nombre}, Cargo: {self.cargo}, Sueldo: {self.sueldo} Bs"


class Empresa:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.empleados = [None] * capacidad
        self.cantidad = 0

    def agregar_empleado(self, empleado):
        self.empleados[self.cantidad] = empleado
        self.cantidad += 1

    def mostrar_empleados(self):
        print(f"\nEmpresa: {self.nombre}")
        for i in range(self.cantidad):
            print(self.empleados[i])


def validar_cargo(cargo):
    if not cargo.replace(" ", "").isalpha():
        raise CargoInvalidoException(
            "El cargo solo debe contener letras."
        )


def validar_sueldo(sueldo):
    if sueldo < 2500:
        raise SueldoInvalidoException(
            "Sueldo menor al salario minimo."
        )


nombre_empresa = input("Nombre de la empresa: ")
n = int(input("Cantidad de empleados: "))

empresa = Empresa(nombre_empresa, n)

for i in range(n):
    print(f"\nEmpleado {i + 1}")

    nombre = input("Nombre: ")

    while True:
        try:
            cargo = input("Cargo: ")
            validar_cargo(cargo)
            break
        except CargoInvalidoException as e:
            print(e)

    sueldo = float(input("Sueldo: "))

    try:
        validar_sueldo(sueldo)
    except SueldoInvalidoException as e:
        print(e)
        print("Se asignará automáticamente 2500 Bs.")
        sueldo = 2500

    empleado = Empleado(nombre, cargo, sueldo)
    empresa.agregar_empleado(empleado)

empresa.mostrar_empleados()