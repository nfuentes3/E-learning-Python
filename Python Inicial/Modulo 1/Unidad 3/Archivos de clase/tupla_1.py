mi_lista = [1, "a", True]

mi_tupla = (1, "a", True)

print(mi_lista)
print(type(mi_lista))
print(mi_lista[0])
print(mi_tupla)
print(type(mi_tupla))
print(mi_tupla[0])

print("Lista","---" * 23)
print(id(mi_lista))
mi_lista += [2,3]
print(id(mi_lista)) #Mantiene el id (Lista : Mutable)


print("Tupla","---" * 23)
print(id(mi_tupla))
mi_tupla += (2,3)
print(id(mi_lista)) #Cambia el id (Tupla : Inmutable)