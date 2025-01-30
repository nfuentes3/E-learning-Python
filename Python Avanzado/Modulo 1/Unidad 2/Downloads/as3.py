class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre

    def getNombre(self, ):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre


pedro = Usuario("Pedro")
print(pedro.getNombre())
pedro.setNombre("Pedro2")
print(pedro.getNombre())