from modelo_orm import *
from vista import *


if __name__ == "__main__":
    ventana = Tk()
    app = MainVentana(ventana)
    app.actualizar_tree()
    ventana.mainloop()