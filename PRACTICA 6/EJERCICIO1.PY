class Persona:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
class Estudiante(Persona):
    def __init__(self, id, nombre, matricula, carrera):
        super().__init__(id, nombre)
        self.matricula = matricula
        self.carrera = carrera
        self.materias = []
class Docente(Persona):
    def __init__(self, id, nombre, especialidad, salario):
        super().__init__(id, nombre)
        self.especialidad = especialidad
        self.salario = salario
class Materia:
    def __init__(self, nombre, codigo, docente):
        self.nombre = nombre
        self.codigo = codigo
        self.docente = docente
        self.estudiantes = []
        self.notas = []
        self.examenes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        estudiante.materias.append(self)
class Nota:
    def __init__(self, valor, fecha, estudiante, materia):
        self.valor = valor
        self.fecha = fecha
        self.estudiante = estudiante
        self.materia = materia
class Aula:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
class Horario:
    def __init__(self, dia, hora, materia, aula):
        self.dia = dia
        self.hora = hora
        self.materia = materia
        self.aula = aula
class Examen:
    def __init__(self, fecha, tipo):
        self.fecha = fecha
        self.tipo = tipo
class Kardex:
    def __init__(self, semestre, gestion):
        self.semestre = semestre
        self.gestion = gestion
        self.materias = []
        self.estudiantes = []
        self.docentes = []
    def agregar_materia(self, materia):
        self.materias.append(materia)

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def agregar_docente(self, docente):
        self.docentes.append(docente)
