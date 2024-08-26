""" Crear una función lambda que sea equivalente a la siguiente función:
def sumar(valor1, valor2):
    res = valor1 + valor2
    return res"""

sumar = lambda valor1, valor2 : valor1 + valor2

num1 = int(input("Indique el primer valor: "))
num2 = int(input("Indique el primer valor: "))

print("Resultado:",sumar(num1,num2))