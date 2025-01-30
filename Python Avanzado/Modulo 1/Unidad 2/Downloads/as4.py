class Usuario:

    def __init__(self, nombre):
        self._nombre = nombre
    
    def get_nombre(self, ):
        print("Estoy dentro de la obtención del nombre")
        return self._nombre

    def set_nombre(self, nombre):
        print("Estoy seteando el nombre")
        self._nombre = nombre

    def del_nombre(self):
        print("Voy a borrar el nombre")
        del self._nombre

    nombre=property(get_nombre, set_nombre, del_nombre, "Datos extra")

pedro = Usuario("Pedro")
print(pedro.nombre)
pedro.nombre="Pedro2"
print(pedro.nombre)