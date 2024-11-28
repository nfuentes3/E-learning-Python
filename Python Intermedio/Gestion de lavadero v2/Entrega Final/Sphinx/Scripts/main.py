"""
    Ejecución de la app:
    ---------------------
    
    La ejecución del modulo 'main.py' lanza la aplicación.
"""
#Modulos internos
from controlador import *


if __name__ == "__main__":
    """
        Ejecuta el script principal del programa.
        --- Main --- 
            -Crea instancia de la clase Controller.
            -Crea instancia de la clase OperacionesDB para la conexion con la base de datos.
            -Llama a la funcion de tkinter mainloop de la clase ventana.
    """
    app = Controller()
    db = OperacionesDB()
    app.ventana.mainloop()
