from abc import ABC, abstractmethod
import math
class Figura(ABC):
    def __init__(self, color):
        self.color = color
    @abstractmethod
    def obtenerArea(self):
        pass
class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado
    def obtenerArea(self):
        return self.lado * self.lado
class Triangulo(Figura):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def obtenerArea(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return area
class Redondo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio
    def obtenerArea(self):
        return math.pi * self.radio * self.radio
c1 = Cuadrado("rojo", 4)
c2 = Cuadrado("azul", 6)
t1 = Triangulo("verde", 3, 4, 5)
t2 = Triangulo("amarillo", 5, 5, 6)
r1 = Redondo("negro", 3)
r2 = Redondo("blanco", 5)
print("Área cuadrado 1:", c1.obtenerArea())
print("Área cuadrado 2:", c2.obtenerArea())
print("Área triangulo 1:", t1.obtenerArea())
print("Área triangulo 2:", t2.obtenerArea())
print("Área redondo 1:", r1.obtenerArea())
print("Área redondo 2:", r2.obtenerArea())
def mayor_area(fig1, fig2):
    if fig1.obtenerArea() > fig2.obtenerArea():
        return fig1.color
    elif fig2.obtenerArea() > fig1.obtenerArea():
        return fig2.color
    else:
        return "Empate"
resultado = mayor_area(c1, t1)
print("La figura con mayor área tiene color:", resultado)