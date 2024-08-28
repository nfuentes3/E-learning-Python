"""Realice nuevamente los ejercicios de la unidad 1 (3, 4 y 5), pero tratando de utilizar una
función, de forma que la operación se realice dentro de la misma.
Presente el resultado en la terminal del editor."""

#Ejercicio 5 U1
"""Escriba un programa que solicite un valor entero por pantalla y presente en la terminal
editor el valor incrementado en un 10%."""

def diez_por_ciento (numero):
    resultado = numero * 1.1
    print("Sumando un 10% al numero indicado, el resultado es: ", resultado)
    

entrada = int(input("Indique un numero: "))
diez_por_ciento(entrada)
