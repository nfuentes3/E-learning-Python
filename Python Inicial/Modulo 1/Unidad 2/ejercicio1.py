"""Ejercicio 1 (Este es el ejercicio 2 de la unidad 1 pero implementando if/else
Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
son múltiplos de dos. Utilice la estructura if/else
"""

import sys

#
valor1 = int(sys.argv[1])

valor2 = int(sys.argv[2])

valor3 = int(sys.argv[3])

#Se crea condicional, con ejecuion por consola: py ejercicio2.py 2 3 8
if valor1 % 2 == 0:
    print("El número", valor1, "es un numero PAR.")
else:
    print("El número", valor1, "es un numero IMPAR.")

if valor2 % 2 == 0:
    print("El número", valor2, "es un numero PAR.")
else:
    print("El número", valor2, "es un numero IMPAR.")
    
if valor3 % 2 == 0:
    print("El número", valor3, "es un numero PAR.")
else:
    print("El número", valor3, "es un numero IMPAR.")