import random

resultado = 5 * random.randint(0,5)
print(resultado)

if resultado < 11:
    print("Es menor")
else:
    print("Es mayor")