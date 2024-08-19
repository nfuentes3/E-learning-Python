"""Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparece la letra “a”. """

oracion = input("Indique una oración, y te dire cuantas letra 'a' hay en la misma: ").lower() #Se usa .lower para que no discrimine si el usuario usa mayusculas o minusculas.

repeticion = oracion.count('a')

print(f"La cantidad de veces que aparece la letra 'a' en la oracion es de * {repeticion} * veces.")