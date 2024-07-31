"""Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
son múltiplos de dos."""

import sys

# Ejecucion: ejercicio2.py 2 3 8

valor1 = sys.argv[1]
valor1 = int(valor1)
valor2 = sys.argv[2]
valor2 = int(valor2)
valor3 = sys.argv[3]
valor3 = int(valor3)

if valor1 % 2 == 0:
    print("Es un numero par")
else:
    print("Es un numero impar")

if valor2 % 2 == 0:
    print("Es un numero par")
else:
    print("Es un numero impar")

if valor3 % 2 == 0:
    print("Es un numero par")
else:
    print("Es un numero impar")
