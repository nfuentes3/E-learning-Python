"""Se puede utilizar __add__ como ejemplo en un caso donde haya que agregar alguna observacion a una instancia de clase.

Como se puede ver en este caso, se usa para agregar algun tipo de comentario adicional (en caso de que lo desee el cliente) a un pedido de pizza.
"""
class Pizzas:
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
    
    def __str__(self):
        return f"Pedido: {self.nombre} {self.tipo} {self.precio}"
    
    def __add__(self, comentario):
        return f"Pedido: {self.nombre} {self.tipo} {self.precio} | Comentario: {comentario}"

pedido1 = Pizzas("Nicolas", "Muzzarella", 4500)
print(pedido1)

#Agregando comentario dentro del mismo pedido (instancia de clase)
pedido2 = Pizzas("Juan", "Napolitana", 5000)
obs_pedido2 = pedido2 + "Sin ajo"
print(obs_pedido2)