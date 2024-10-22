class Persona():
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def comer_arroz(self):
        print("Comer arroz desde persona")

class Argentinos(Persona):
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def comer_arroz(self):
        print("Comer arroz desde Argentinos con tenedor")

class Chinos(Persona):
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def comer_arroz(self):
        print("Comer arroz desde Chinos con palillos")

anna = Persona("Anna Karen")
juan = Persona("Juan Marcelo")
pepe = Argentinos("Jose Gaston")
josefa = Chinos("Josefa Celeste")

anna.comer_arroz()
juan.comer_arroz()
pepe.comer_arroz()
josefa.comer_arroz()
print(Chinos.__mro__)