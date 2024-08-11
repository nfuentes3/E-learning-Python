"""Realice un programa que consulte la edad y en caso de que el valor ingresado supere la
fecha de jubilación, presente en la terminal el mensaje
caso contrario que presente "Aun está en edad de trabajar". """

print("-" * 30)
print("Indicador de edad jubilatoria:")
print("-" * 30)
#Pedido de edad por consola
edad = int(input("Indique su edad: "))

#Considerando que la edad jubilatoria es mayor a 65 años:
if edad > 65:
    print("Esta en condicion de iniciar la jubilación.")
else:
    print("Aun está en edad de trabajar.")