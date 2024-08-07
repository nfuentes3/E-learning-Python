"""mi_variable = 1
mi_variable2 = "Pera"

mi_lista = [mi_variable, mi_variable2, 1.2, "Limon"]

print(mi_lista)

#Indexacion de lista
print(mi_lista[0], "----", mi_lista[-1])

autos = ["auto1", "auto2"]

#Se puede anidar lista, uniendo dos para hacer uno.
resultado = mi_lista + autos 
print(resultado)
"""

# Practica de lista - datos de persona

persona1 = ["Pepe Guapo Mario", "Perez", 4, "12345678", "3000"]
# print(persona1)

persona2 = ["Anna", "Perez", 12, "12345622", "4300"]
# print(persona2)

persona3 = ["Josefa", "Rodriguez", 45, "134452", "50000"]

personas = [persona1, persona2]
# print(personas)

personas.append(persona3)
# print(personas)

# print(personas[-1])

print(persona1[0].split()[-3])
