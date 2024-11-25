from vista import *
from controlador import *
from modelo import *

if __name__ == "__main__":
    root = Tk()
    vista = MainVista(root)
    modelo = Operaciones()
    
    controlador = Controlador(vista, modelo)
    
    root.mainloop()