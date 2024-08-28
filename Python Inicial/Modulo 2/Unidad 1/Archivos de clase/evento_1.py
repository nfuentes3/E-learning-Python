from tkinter.colorchooser import askcolor
from tkinter import *

master = Tk()

def funcion():
    #ruta = askopenfilename()
    #print(ruta)
    resultado = askcolor(color="#00ff00",title="El titulo" )
    print(resultado)
    print(resultado[1])

boton_g = Button(master, text="Guardar", command=funcion)
boton_g.grid(row=2, column=1)

master.mainloop()