class Personal:

    def __init__(self, nombre, dni):
        self.nombre = nombre
        self._dni = dni
        self.__privado = self._dni + " " + self.nombre


pedro = Personal("Pedro", "12121212")
print(pedro.nombre)
print(pedro._dni)
print(pedro.__dict__)
print(pedro._Personal__privado)