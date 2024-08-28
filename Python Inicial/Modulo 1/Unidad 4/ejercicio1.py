"""Cree una función lamba que compruebe si un número es par o impar."""

par_impar = lambda num1 : num1 % 2 == 0
numero = int(input("Indique un numero: "))
print(f"El numero es par?: {par_impar(numero)}")