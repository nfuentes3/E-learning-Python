class ClasePadre:
    def __init__(self, nombre):
        self.nombre = nombre



class ClaseHija(ClasePadre):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def __str__(self):
        return f"{self.nombre}"

    def __add__(self, apellido):
        return f"{self.nombre} {apellido}"

#Instancia de ClaseHija
objeto1 = ClaseHija("Juan")
print(objeto1)

#Otra instancia para utilizar el metodo __add__
objeto2 = objeto1 + "Perez"
print(objeto2)