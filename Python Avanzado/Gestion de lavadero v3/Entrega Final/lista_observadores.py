class Obervador:
    def update(self):
        raise NotImplementedError("Error al implementar el metodo update")


class ObservadorABM(Obervador):
    def update(self, accion, datos):
        print(f"Accion realizada: {accion}\nDatos recibidos: {datos}")
