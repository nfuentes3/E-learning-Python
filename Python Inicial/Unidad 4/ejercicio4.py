"""Crear una función lambda que tome como parámetro una frase y la escriba al revés."""

frase_reves = lambda frase : frase [-1::-1]

print(frase_reves(input("Ingrese la frase: ")))