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

# Muestra de resultados
print("El numero si es par mostrara True si es impar mostrara False:")
print("Numero", valor1, ":", valor1 % 2 == 0)
print("Numero", valor2, ":", valor2 % 2 == 0)
print("Numero", valor3, ":", valor3 % 2 == 0)
