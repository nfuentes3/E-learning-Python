x  = "curso"

while x:
    print(x)
    x = x[1:] #Recorre todo los elementos del string hasta finalizarlo
    
print("---" * 23)

a = 1
b = 7

while a < b:
    print(a)
    a += 1 #Incremento de valor
    
print("---" * 23)

lista = [1, 2, 3, 4]

while lista:
    c, *lista = lista
    print(c, lista)