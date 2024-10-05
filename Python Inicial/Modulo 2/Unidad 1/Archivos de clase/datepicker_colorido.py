from tkinter import *
from tkcalendar import *

master = Tk()
master.geometry("300x300")
master.title("Tarea Opcional 3")

calendario = Calendar(
    master,
    selectmode="day",
    background="black",
    selectbackground="blue",
    normalbackground="pink",
    weekendbackground="yellow",
    othermonthbackground="red",
    othermonthwebackground="green",
)
calendario.grid(row=1, column=1)


def elegir():
    resultado = calendario.get_date()
    print(type(resultado))
    print(f"El dia elegido es: {resultado}")


aceptar = Button(master, text="Aceptar", command=elegir, bg="black", fg="white")
aceptar.grid(row=3, column=1)

master.mainloop()
