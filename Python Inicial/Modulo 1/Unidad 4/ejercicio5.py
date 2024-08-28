"""Cree un programa que utilizando una función, solicite la edad de la persona e imprima todos los años que la persona ha cumplido según el siguiente formato de ejemplo:
1, 2, 3, 4, 5
Y
5, 4, 3, 2, 1 """

def mostrar_edad():
    edad = int(input("Ingese su edad: "))
    
    for i in range(0, edad + 1): # (Desde, hasta (se pone +1 para que muestre el ulitmo valor))
        print(i , end = ", ")
    
    print("\nY")
    
    for i in range(edad, 0, -1): # (Desde, hasta, secuencia)
        print(i , end = ", ")

mostrar_edad()