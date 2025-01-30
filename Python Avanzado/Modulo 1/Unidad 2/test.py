# Hacemos un diccionario que contenga los requisitos de edad según género:

edad_jubilatoria = {
    "hombre": 65,
    "mujer": 60
}

class DescriptorEmpleados:
    def __get__(self, instance, owner):
        return instance._edad, instance._genero
    
    def __set__(self, instance, value):
        edad, genero = value
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        elif genero == "hombre":
            if edad == edad_jubilatoria["hombre"] - 1:
                print("Falta un año para jubilarse:")
                print(type(edad))
        elif genero == "mujer":
            if edad == edad_jubilatoria["mujer"] - 1:
                print("Falta un año para jubilarse:")
        else:
            pass
        instance._edad = edad
        instance._genero = genero

class Empleados:
    edad_genero = DescriptorEmpleados()
    
    def __init__(self, nombre, edad, genero, salario):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.salario = salario
    
    @property
    def edad(self):
        return self._edad
    
    @property
    def genero(self):
        return self._genero
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Salario: {self.salario}\n **********"


try:
    empleado1 = Empleados("Juan", -1, "hombre", 1000)
    print(empleado1)
except ValueError as e:
    print(e)

try:
    empleado2 = Empleados("Carlos", 64, "hombre", 23000)
    print(empleado2)
except ValueError as e:
    print(e)

try:
    empleado3 = Empleados("Maria", 59, "mujer", 22000)
    print(empleado3)
except ValueError as e:
    print(e)


try:
    empleado4 = Empleados("Pablo", 24, "hombre", 13000)
    print(empleado4)
except ValueError as e:
    print(e)