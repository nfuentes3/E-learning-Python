"""Consigna: Cree un programa que tome tres valores por consola multiplique el primero por el segundo
y le sume el tercero. Presente el resultado en la terminal del editor."""

valor1 = input("Indique el primer valor: ")
valor1 = int(valor1)

valor2 = input("Indique el segundo valor: ")
valor2 = int(valor2)

valor3 = input("Indique el tercer valor: ")
valor3 = int(valor3)

resultado = (valor1 * valor2) + valor3
resultado = str(resultado)

print("El resultado es: " + resultado)
