class Animal:
    def __init__(self, nom, edad, due):
        self.nom = nom
        self.edad = edad
        self.due = due


class Perro(Animal):
    def __init__(self, nom, edad, due, bolsa, ladra):
        super().__init__(nom, edad, due)
        self.bolsa = bolsa
        self.ladra = ladra


class Gato(Animal):
    def __init__(self, nom, edad, due, caza, leche):
        super().__init__(nom, edad, due)
        self.caza = caza
        self.leche = leche


class CentroVet:
    def __init__(self, nom):
        self.nom = nom
        self.perros = [None] * 100
        self.gatos = [None] * 100
        self.cant_p = 0
        self.cant_g = 0

    def add_perro(self, p):
        if self.cant_p < 100:
            self.perros[self.cant_p] = p
            self.cant_p += 1

    def add_gato(self, g):
        if self.cant_g < 100:
            self.gatos[self.cant_g] = g
            self.cant_g += 1

    def ord_perros(self):
        arr = [self.perros[i] for i in range(self.cant_p)]
        arr.sort(key=lambda x: (x.edad, x.due, x.nom))
        for i in range(self.cant_p):
            self.perros[i] = arr[i]

    def ord_gatos(self):
        arr = [self.gatos[i] for i in range(self.cant_g)]
        arr.sort(key=lambda x: (not x.leche, -x.edad, x.nom))
        for i in range(self.cant_g):
            self.gatos[i] = arr[i]

    def mismos_due(self):
        todos = [None] * (self.cant_p + self.cant_g)
        cant_todos = 0

        for i in range(self.cant_p):
            todos[cant_todos] = self.perros[i]
            cant_todos += 1

        for i in range(self.cant_g):
            todos[cant_todos] = self.gatos[i]
            cant_todos += 1

        for i in range(cant_todos):
            if todos[i] is None:
                continue

            nom_due = todos[i].due
            cont = 1

            for j in range(i + 1, cant_todos):
                if todos[j] is not None and todos[j].due == nom_due:
                    cont += 1
                    todos[j] = None

            if cont > 1:
                print("Dueño:", nom_due, "tiene", cont, "animales")


c1 = CentroVet("Centro 1")
c2 = CentroVet("Centro 2")

c1.add_perro(Perro("Rex", 5, "Juan", True, True))
c1.add_perro(Perro("Max", 3, "Ana", False, True))
c1.add_gato(Gato("Michi", 2, "Juan", True, True))
c1.add_gato(Gato("Luna", 4, "Luis", False, False))

c2.add_perro(Perro("Rocky", 6, "Pedro", True, False))
c2.add_perro(Perro("Toby", 2, "Pedro", False, True))
c2.add_gato(Gato("Nina", 1, "Sofia", True, True))
c2.add_gato(Gato("Kira", 3, "Pedro", False, True))

c1.ord_perros()
c1.ord_gatos()

print("Perros ordenados Centro 1:")
for i in range(c1.cant_p):
    p = c1.perros[i]
    print(p.nom, p.edad, p.due)

print("Gatos ordenados Centro 1:")
for i in range(c1.cant_g):
    g = c1.gatos[i]
    print(g.nom, g.edad, g.due, g.leche)

print("Dueños con varios animales en Centro 1:")
c1.mismos_due()

print("Dueños con varios animales en Centro 2:")
c2.mismos_due()