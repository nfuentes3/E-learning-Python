from tkinter import *
from tkinter.colorchooser import askcolor

master = Tk()
master.geometry("290x130") #Tamaño predefinido de ventana


def mostar_alta(): #Funcion que imprime los entrys
    print("Nueva alta de datos: ")
    print(entry_titulo.get(), entry_ruta.get(), entry_descripcion.get())

def sorpresa(): #Funcion que cambia color de la ventana master
    color_elegido = askcolor(color="#00ff00",title="Seleccione un color" )
    master.configure(background=color_elegido[1])

#Agregando paddings a columnas para mejorar visualización
master.grid_columnconfigure(0, pad=15)
master.grid_columnconfigure(2, pad=40)
master.grid_rowconfigure(3, pad=20)

#Labels y entradas
titulo = Label(master, text="Título")
titulo.grid(row=0, column=0, sticky=W)
entry_titulo = Entry(master)
entry_titulo.grid(row=0,column=1)

ruta = Label(master, text="Ruta")
ruta.grid(row=1, column=0, sticky=W)
entry_ruta = Entry(master)
entry_ruta.grid(row=1,column=1)

descripcion = Label(master, text="Descripcion")
descripcion.grid(row=2, column=0, sticky=W)
entry_descripcion = Entry(master)
entry_descripcion.grid(row=2,column=1)

#Botones
boton_alta = Button(master, text="Alta", command=mostar_alta, padx=10, pady=5)
boton_alta.grid(row=1, column=2)

boton_sorpresa = Button(master, text="Sorpresa", command=sorpresa, padx=10, pady=5)
boton_sorpresa.grid(row=3, column=1)

master.mainloop()