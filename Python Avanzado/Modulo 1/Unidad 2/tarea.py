#Considerando que la edad jubilatoria para cualquier genero es a los 60 años

class DescriptorEmpleados:
    def __get__(self, instance, owner):
        print("***")
        print("Empleado:")
        print(f"Nombre: {instance.nombre}, Edad: {instance.edad}, Salario: {instance.salario}")
        try:
            if instance.edad == 59:
                print("***Esta a un año de jubilarse***")
            elif instance.edad < 0:
                raise ValueError("Error al indicar la edad (No debe ser menor que cero)")
        except ValueError as e:
            print(e)
        return instance.nombre, instance.edad, instance.salario

class Empleados:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    
    empleado = DescriptorEmpleados()



empleado1 = Empleados("Jose", 59, 24000)
empleado2 = Empleados("Nico", 30, 20000)
empleado3 = Empleados("Ana", -1, 15000)
print(empleado1.empleado)
print(empleado2.empleado)
print(empleado3.empleado)