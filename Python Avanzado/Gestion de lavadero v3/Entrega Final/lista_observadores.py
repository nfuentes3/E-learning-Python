class Observador:
    def update(self):
        raise NotImplementedError("Error de implementacion del Observador")

class ObservadorABM(Observador):
    def update(self, accion, datos):
        print("***"*10)
        print(f"Acción realizada: {accion}\nDatos recibidos: {datos}")
        print("***"*10)