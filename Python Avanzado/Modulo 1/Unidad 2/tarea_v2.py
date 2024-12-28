#Genero un diccionario para determinar la edad jubilatoria segun sexo.
edad_jubilatoria = {
    "hombre": 65,
    "mujer": 60
}

class Empleados:
    
    class DescriptorEmpleados:
        def __get__(self, instance, owner):
            return instance.edad, instance.sexo

        def __set__(self, instance, valor):
            instance.edad = valor
            if instance.sexo == "hombre":
                if valor == edad_jubilatoria['hombre'] -1:
                    print("Falta un año para jubilarse")
            elif instance.sexo == "mujer":
                if valor == edad_jubilatoria['mujer'] -1:
                    print("Falta un año para jubilarse")

    def __init__(self, nombre, edad, sexo, salario):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa (menor a 0)")
        else:
            self.nombre = nombre
            self.sexo = sexo
            self.salario = salario
            self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}, Salario: {self.salario}"

    descriptor = DescriptorEmpleados()

try:
    print("***"*20)
    persona1 = Empleados("Juan", 23, "hombre", 1000)
    persona1.descriptor = 64
    print(persona1)
except ValueError as e:
    print(e)

try:
    print("***"*20)
    persona2 = Empleados("Claudia", 23, "mujer", 3000)
    persona2.descriptor = 59
    print(persona2)
except ValueError as e:
    print(e)

try:
    print("***"*20)
    persona3 = Empleados("Jose", -1, "hombre", 2000)
    print(persona3)
except ValueError as e:
    print(e)


try:
    print("***"*20)
    persona3 = Empleados("Nico", 29, "hombre", 2000)
    print(persona3)
except ValueError as e:
    print(e)   