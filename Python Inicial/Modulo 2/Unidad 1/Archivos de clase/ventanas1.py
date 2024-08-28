from tkinter import * 
from tkinter.messagebox import *

master = Tk()

def funcion_e():
    showerror("Titulo de mensaje de error", "Contenido del mensaje")
    

def funcion_s():
    if askyesno("Titulo de la consulta de verificacion", "Contenido de la consulta"):
        showinfo("Si", "Mensaje de información")
    else:
        showinfo("No", "Esta a punto de salir")

boton_e = Button(master, text="Error", command=funcion_e)
boton_e.grid(row=0, column=1)

boton_s = Button(master, text="Show", command=funcion_s)
boton_s.grid(row=2, column=1)

master.mainloop()