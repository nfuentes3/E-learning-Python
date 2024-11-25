from vista import *
from modelo import *

class Controlador:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        self.db = MainVista()
        self.op = Operaciones()
        self.acciones()

    def acciones(self):
        self.db.boton.config(command=self.op.printar())