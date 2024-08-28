"""Suponga que tiene una verdulería y carga la cantidad y el precio de lo comprado por un cliente. 
Realice un programa que tome de a uno la cantidad y el precio comprado por el cliente y al finalizar la compra retorne el monto total gastado. 
"""

def verduleria(): #Creo el programa directamente dentro de una función.
    compra = True #Inicializo la condicion para el bucle de la compra.
    total = 0 #Inicializo total de la compra.
    
    while compra == True:
        producto = input("Que es lo que quiere llevar?: ")
        kg = float(input("Cuantos kilos quiere?: "))
        precio_unidad = float(input("Cuanto vale por kilo?: "))
        precio_final = kg * precio_unidad
        
        total += precio_final
        
        decision_cliente = input("Desea llevar algo mas? (Y/N): ").lower() #Se crea condicion de si quiere llevarse otro producto, que lo define el booleano de la variable 'compra'.
        if decision_cliente == "y":
            compra = True
        else:
            compra = False

    print(f"El total de la compra es de: ${total} pesos.")


verduleria()