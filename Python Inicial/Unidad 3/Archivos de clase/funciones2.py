lista = [1, 1, 0, 0, 1, 8, 7]

def repetidos(elementos, lista):
    veces = 0
    for i in lista: 
        if elementos == i:
            veces += 1
    return veces

print(repetidos(1, lista))
print(repetidos(0, lista))