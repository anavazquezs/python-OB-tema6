class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    

c1 = Coche("Rojo", 4, 3, 100, 4)

print("El color del coche es: ", c1.color, ", tiene ", c1.puertas, " puertas y la cilindrada es: ", c1.cilindrada)