from modelo import *
from vista import *


if __name__ == "__main__":
    db = OperacionesDB()
    ventana = Tk()
    app = MainVentana(ventana)
    tree = AccionesBTN(ventana)
    tree.actualizar_tree()
    ventana.mainloop()