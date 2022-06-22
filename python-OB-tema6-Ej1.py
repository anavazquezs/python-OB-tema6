class Vehiculo:
    color = "Rojo"
    ruedas = 4
    puertas = 3

class Coche(Vehiculo):
    velocidad = 180
    cilindrada = 4
    

c1 = Coche()

print("El color del coche es: ", c1.color, ", tiene ", c1.puertas, " puertas y la cilindrada es: ", c1.cilindrada)