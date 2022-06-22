class Alumno:
    aprobado = None
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
    
    def condicion(self):
        if (self.calificacion >= 7):
            self.aprobado = True
        else:
            self.aprobado = False
    
    def isAprobado(self):
        return self.aprobado

a1 = Alumno("Oscar", 8)
a1.condicion()
a2 = Alumno("Verena", 5)
a2.condicion()

print("El estudiante: ", a1.nombre, " ha obtenido una calificación de: ", a1.calificacion, ". Condición aprobado? ", a1.aprobado)

print("El estudiante: ", a2.nombre, " ha obtenido una calificación de: ", a2.calificacion, ". Condición aprobado? ", a2.aprobado)