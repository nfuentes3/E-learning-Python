"""Tome el ejercicio de cálculo de números pares e impares de la unidad 2 y agréguele un bucle al código de forma de simplificarlo. """
import sys

#Se crea condicional, con ejecuion por consola: py ejercicio2.py 2 3 8
for numero in sys.argv[1:]:
    valor = int(numero)
    
    if valor % 2 == 0:
        print(f"El numero {valor} es un numero PAR.")
    else:
        print(f"El numero {valor} es un numero IMPAR.")