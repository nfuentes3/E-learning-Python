from tkinter import *

class MainVista:
    def __init__(self, ventana):
        self.master = ventana
        self.master.title("test")
        
        
        self.titulo = Label(self.master, text="Texto de prueba")
        self.titulo.grid(column=0, row=0)
        
        self.boton = Button(self.master, text="Apreta")
        self.boton.grid(column=0, row=1)
