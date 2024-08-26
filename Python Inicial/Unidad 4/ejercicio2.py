"""Crear una función lambda que sea equivalente a la siguiente función:
def multiplicar_por_tres(valor):
    res = 3 * valor
    return res """

multiplicar_por_tres = lambda valor: valor * 3

numero = int(input("Indique un numero a multiplicar por 3: "))

print(f"El resultado es:",multiplicar_por_tres(numero))
