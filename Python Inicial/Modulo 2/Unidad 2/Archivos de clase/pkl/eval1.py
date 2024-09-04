lista = ["[1,2,3]","['Pera','Limon']\n","{'id': 1, 'nombre' : 'Anna'}"]
print(lista)
print(lista[0])
print(type(lista[0]))

objeto0 = eval(lista[0])
print(objeto0)
print(type(objeto0))

objeto1 = eval(lista[1])
print(objeto1)
print(type(objeto1))

objeto2 = eval(lista[2])
print(objeto2)
print(type(objeto2))