"""Tome el ejercicio de cálculo de números pares e impares de la unidad 2 y agréguele un bucle al código de forma de simplificarlo. """

import sys

valores = int(sys.argv[1])


#Se crea condicional, con ejecuion por consola: py ejercicio1.py 2 3 8
for numero in valores:
    if valores % 2 == 0:
        print("Es un numero par.")
    else:
        print("Es un numero impar.")
