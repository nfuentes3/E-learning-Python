"""Realice nuevamente los ejercicios de la unidad 1 (3, 4 y 5), pero tratando de utilizar una
función, de forma que la operación se realice dentro de la misma.
Presente el resultado en la terminal del editor."""

#Ejercicio 3 U1
"""Escriba un programa que solicite el radio de una circunferencia y permita calcular el perímetro.
Presente el resultado en la terminal del editor."""

print("Calculador de perimetro")
print("-" * 20)

def longitud (radio):
    perimetro = 2 * 3.1416 * radio
    print("El perimetro de la circunferencia segun el radio indicado es: ", perimetro)
    print("-" * 20)


entrada = int(input("Indique el radio de una circunferencia: "))
longitud(entrada)