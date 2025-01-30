class Usuario:

    def __init__(self, nombre):
        self._nombre = nombre
    
    @property
    def nombre(self, ):
        "Datos extra"
        print("Estoy dentro de la obtención del nombre")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Estoy seteando el nombre")
        self._nombre = nombre

    @nombre.deleter
    def nombre(self):
        print("Voy a borrar el nombre")
        del self._nombre


pedro = Usuario("Pedro")
print(pedro.nombre)
pedro.nombre="Pedro2"
print(pedro.nombre)