"""Tome dos valores por consola, y guarde en una lista:
[primer_valor, segundo_valor, la_suma_de_los_valores]
Presente el resultado en la terminal del editor."""

#Se piden los dos primeros valores por consola.
primer_valor = int(input("Indique el primer numero: "))
segundo_valor = int(input("Indique el segundo numero: "))

lista = [] #Se crea una lista vacía.

#Se agrega los tres 2 valores indicados por consola
lista.append(primer_valor)
lista.append(segundo_valor)
#Se hace la suma de los primeros dos valores par que corresponda al tercer elemento de la lista.
lista.append(primer_valor + segundo_valor)

print(lista)