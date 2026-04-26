class Libro:
    def __init__(self, nom, aut, anio):
        self.nom = nom
        self.aut = aut
        self.anio = anio
    def ver(self):
        return f"{self.nom} - {self.aut} ({self.anio})"
class Biblioteca:
    def __init__(self, nom):
        self.nom = nom
        self.libros = [None] * 100
        self.cant = 0
    def add_libro(self, lib):
        if self.cant < 100:
            self.libros[self.cant] = lib
            self.cant += 1
    def buscar(self, nom_lib):
        for i in range(self.cant):
            if self.libros[i].nom.lower() == nom_lib.lower():
                print(f" Libro encontrado en {self.nom}:")
                print(self.libros[i].ver())
                return
        print(f" El libro '{nom_lib}' NO está en {self.nom}")
    def mostrar(self):
        print(f"\n Biblioteca: {self.nom}")
        print(f"Cantidad de libros: {self.cant}")
        print("Libros:")
        for i in range(self.cant):
            print("-", self.libros[i].ver())
b1 = Biblioteca("Central")
b2 = Biblioteca("Zona Sur")
b1.add_libro(Libro("POO", "Perez", 2020))
b1.add_libro(Libro("Python", "Lopez", 2021))
b2.add_libro(Libro("Java", "Diaz", 2019))
b2.add_libro(Libro("C++", "Mora", 2018))
b1.buscar("POO")
b2.buscar("POO")
if b1.cant > b2.cant:
    print("\n Biblioteca con más libros:")
    b1.mostrar()
elif b2.cant > b1.cant:
    print("\n Biblioteca con más libros:")
    b2.mostrar()
else:
    print("\n Empate entre bibliotecas:")
    b1.mostrar()
    b2.mostrar()