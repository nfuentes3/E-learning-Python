"""A partir del ejercicio 5 cree un programa que vaya agregando en una lista las compras realizadas."""

def verduleria(): #Creo el programa directamente dentro de una función.
    compra = True #Inicializo la condicion para el bucle de la compra.
    total = 0 #Inicializo total de la compra.
    lista = [] #Inicializo lista de compras.
    
    while compra == True:
        producto = input("Que es lo que quiere llevar?: ")
        kg = float(input("Cuantos kilos quiere?: "))
        precio_unidad = float(input("Cuanto vale por kilo?: "))
        precio_final = kg * precio_unidad
        lista_compra = []
        
        total += precio_final
        lista.append(lista_compra)
        
        decision_cliente = input("Desea llevar algo mas? (Y/N): ").lower() #Se crea condicion de si quiere llevarse otro producto, que lo define el booleano de la variable 'compra'.
        if decision_cliente == "y":
            compra = True
        else:
            compra = False
        lista_compra.append((producto, kg, precio_unidad))

    print(f"El total de la compra es de: ${total} pesos.")
    print(f"Lista de compras:\n{lista}")


verduleria()