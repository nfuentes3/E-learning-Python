class Operaciones:
    def __init__(self, numero):
        self.numero = numero
    
    def __str__(self):
        return f"Numero: {self.numero}"
    
    def __sub__(self, numero2):
        return Operaciones(self.numero - numero2)
    
    def __mul__(self, numero3):
        return Operaciones(self.numero * numero3)
    
    def __le__(self, numero4):
        return (Operaciones(self.numero <= numero4))

numero1 = Operaciones(10)
print(numero1)
resta = numero1 - 5
print(f"__sub__ => {resta}")
multiplica = numero1 * 3
print(f"__mul__ => {multiplica}")
menor = numero1 <= 2
print(f"__le__ => {menor}")
