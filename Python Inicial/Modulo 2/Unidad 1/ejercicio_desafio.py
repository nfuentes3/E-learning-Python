from tkinter import *

master = Tk()
def mostar_alta(): #Funcion que imprime los entrys
    print("Nueva alta de datos: ")
    print(entry_titulo.get(), entry_ruta.get(), entry_descripcion.get())

def sorpresa(): #Funcion que cambia color de la ventana master
    master.configure(background="#E6DDB4")

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
boton_alta = Button(master, text="Alta", command=mostar_alta)
boton_alta.grid(row=3, column=1)

boton_sorpresa = Button(master, text="Sorpresa", command=sorpresa)
boton_sorpresa.grid(row=3, column=2)

master.mainloop()