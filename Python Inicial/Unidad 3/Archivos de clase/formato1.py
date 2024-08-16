entero1 = 3
entero2 = 21
lista1 = [True, "Pera"]

"""print(entero1, entero2, lista1)
#Agregando funcion sep=
print(entero1, entero2, lista1, sep=" / ")
#Agregando salto de linea
print(entero1, entero2, lista1, sep=" / ", end="!\n")
#Agregando tabulacion
print(entero1, entero2, lista1, sep=" / ", end="!\t")
"""

#Obteniendo elementos de la lista por posicion, mediante variables(Asosiación de posicion).
print(lista1)
a, b, c = [True, "Pera", 4]
print(a, b, c)

#Si no conozco elementos de la lista
a, *b = [True, "Pera", 4]
print(a, b, type(b))
#Si tengo un string
a, *b = "Pera"
print(a, b, type(b))

