socios = ["Juan", "Pedro", "Susana", "Ana", "Sofia", "Pablo"]
ajedrez = ["Pedro", "Susana", "Ana", "Sofia", "Pablo"]
natacion = ["Juan", "Pedro", "Susana"]

resultado = set(ajedrez).intersection(set(natacion)) #Personas que fueron a ajedrez y natacion jutnas
print(resultado)
print(type(resultado))