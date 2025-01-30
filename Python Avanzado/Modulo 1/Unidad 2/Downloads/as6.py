class DescriptorUsuario(): 

    "Datos extra"
    def __get__(self, instance, owner):
        print("Estoy dentro de la obtención del nombre")
        print(self, instance, owner)
        return instance._nombre

    def __set__(self, instance, nombre):
        print("Estoy seteando el nombre")
        instance._nombre = nombre

    def __delete__(self, instance):
        print("Voy a borrar el nombre")
        del instance._nombre

class Usuario:

    def __init__(self, nombre):
        self._nombre = nombre

    nombre = DescriptorUsuario()
    

pedro = Usuario("Pedro")
print(pedro.nombre)
pedro.nombre="Pedro2"
print(pedro.nombre)