#Ejercicio 1
class Vehiculos:
    
    def __init__(self, color, matricula, vel_maxima):
        self.color = color
        self.matricula = matricula
        self.vel_maxima = vel_maxima

#Ejercicio 2
    def imprimir(vehiculo):
        print(f"Vehiculo => Color: {vehiculo.color} / Matricula: {vehiculo.matricula} / Velocidad Maxima: {vehiculo.vel_maxima}")


#Ej 1
auto = Vehiculos("Rojo","WWW 123","100km/h")
moto = Vehiculos("Negro", "ABC 987", "120km/h")
lancha = Vehiculos("Azul","HKI 456", "110km/h")

print(auto.color, auto.matricula, auto.vel_maxima)
print(moto.color, moto.matricula, moto.vel_maxima)
print(lancha.color, lancha.matricula, lancha.vel_maxima)

#Ej 2
print(Vehiculos.__mro__)
Vehiculos.imprimir(auto)
Vehiculos.imprimir(moto)
Vehiculos.imprimir(lancha)


class Trenes(Vehiculos):

    def __init__(self, color, matricula, vel_maxima):
        super().__init__(color, matricula, vel_maxima)



simple = Trenes("Verde", "123 HIW", "150km/h")
rapido = Trenes("Negro", "456 TRE", "200km/h")
print(Trenes.__mro__)
Trenes.imprimir(simple)
Trenes.imprimir(rapido)