"""A partir del ejerció 7 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada
"""

total = 0 #Inicializo total de la compra.
lista = [] #Inicializo lista de compras.

def alta():
    producto = input("Que es lo que quiere llevar?: ")
    kg = float(input("Cuantos kilos quiere?: "))
    precio_unidad = float(input("Cuanto vale por kilo?: "))
    precio_final = kg * precio_unidad
    compras_diccionario = {'producto': producto, 'kilos': kg, 'precio' : precio_unidad,'total' : precio_final} #Se crea el diccionario con claves pre-definidas y los valores son las variables de los ingresos del usuario.
    lista.append(compras_diccionario) #Se anida el diccionario dentro de la lista.

def consulta():
    print(lista)

def baja():
    compra = int(input("Cual compra desea eliminar? Indique su indice: "))
    del lista[compra]

def modificar(): #Para la modificacion, se considera directamente eliminar el indice indicado, y crear uno nuevo.
    compra = int(input("Seleccione la compra a modificar: "))
    del lista[compra] 
    alta()

print("Bienvendio al gestor de verduleria:")
cliente = True
while cliente == True:
    print("---" * 23)
    print("Elige alguna de las siguientes opciones: ")
    print("A) Alta de compra")
    print("B) Baja de compra")
    print("C) Consulta de compras realizadas")
    print("D) Modificacion de compra.")
    print("Sino, presione cualquier otra tecla para salir.\n")
    opcion = str(input("Opcion: ")).lower()
    
    if opcion == "a":
        alta()
    elif opcion == "b":
        baja()
    elif opcion == "c":
        consulta()
    elif opcion == "d":
        modificar()
    else:
        print("***" * 23)
        print("Hasta la proxima!")
        print("***" * 23)
        break