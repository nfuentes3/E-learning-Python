oracion = input("Indique una oración, y te diré cuantas vocales aparecen: ").lower()

lista = [] #Inicializando lista para agregar cracacteres encontradas en la lista.
vocales = ['a','e','i','o','u','á','é','í','ó','ú'] #Indicando por lista las vocales a seleccionar.

for letras in oracion:
    if letras in vocales:
        lista.append(letras)

print("-" * 23)
print(f"La cantidad de vocales en la oración es de: {len(lista)} vocales.")