class Personas():
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def comer_arroz(self):
        pass

anna = Personas("Anna Karen")
juan = Personas("Juan Marcelo")

print(anna.nombre)
print(type(anna.nombre))
print(juan.nombre)
print(type(juan.nombre))
