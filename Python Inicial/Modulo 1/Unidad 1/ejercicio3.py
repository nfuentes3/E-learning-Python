"""Escriba un programa que solicite el radio de una circunferencia y permita calcular el perímetro.
Presente el resultado en la terminal del editor."""

print("Calculador de perimetro")
print("-" * 20)
radio = input("Por favor, indique el radio de la circunferencia: ")
radio = int(radio)

longitud = 2 * 3.1416 * radio

print("El perimetro de la circunferencia es de:", longitud)
