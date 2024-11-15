from tkinter import Tk, Label, Entry, Button, ttk, StringVar
import datetime
from modelo import alta_orden, actualizar_tree, crear_tabla, borrar_orden, modificar_orden, consulta_nombre, balance_total
from tkinter.colorchooser import askcolor

master = Tk()
master.geometry("770x700")
master.title("Lavadero - Calle Falsa 123")

crear_tabla()

#Inicializando variables de Tkinter
v_nombre, v_telefono, v_tipo, v_cantidad, v_precio, v_fecha_entrega, v_consulta, v_balance = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()


########## VISTA ##########
#Encabezado
encabezado = Label(master, text="Gestor de ordenes", bg="#2664FA", fg="white")
encabezado.grid(row=0, column=0, columnspan=8, sticky="we")
#Fecha y hora
"""fecha = datetime.now()
fecha_format_pantalla = fecha.strftime("%d/%m/%Y    %H:%M")
fecha_label = Label(master, text=f"{fecha_format_pantalla}")
fecha_label.grid(row=1, column=4, sticky="w" ,padx=20)"""
#Seccion alta
titulo_alta = Label(master, text="Generar o modificar orden:")
titulo_alta.grid(row=1, column=0, sticky="w" ,padx=20)
#Nombre
nombre = Label(master, text="Nombre", bg="#01F56A")
nombre.grid(row=2, column=0,sticky="w", padx=20, pady=7)
entry_nombre = Entry(master, textvariable=v_nombre)
entry_nombre.grid(row=2, column=1,sticky="w")
#Telefono
telefono = Label(master, text="Telefono", bg="#01F56A")
telefono.grid(row=3, column=0, sticky="w", padx=20, pady=7)
entry_telefono = Entry(master, textvariable=v_telefono)
entry_telefono.grid(row=3, column=1, sticky="w")
#Tipo de lavado
tipo = Label(master, text="Tipo de lavado", bg="#01F56A")
tipo.grid(row=4, column=0, sticky="w", padx=20, pady=7)
entry_tipo = Entry(master, textvariable=v_tipo)
entry_tipo.grid(row=4, column=1, sticky="w")
#Cantidad de valet
cantidad = Label(master, text="Cantidad", bg="#01F56A")
cantidad.grid(row=5, column=0, sticky="w", padx=20, pady=7)
entry_cantidad = Entry(master, textvariable=v_cantidad)
entry_cantidad.grid(row=5, column=1, sticky="w")
#Fecha de entrega
fecha_entrega = Label(master, text="Fecha de entrega", bg="#01F56A")
fecha_entrega.grid(row=6, column=0, sticky="w", padx=20, pady=7)
entry_fecha_entrega = Entry(master, textvariable=v_fecha_entrega)
entry_fecha_entrega.grid(row=6, column=1, sticky="w")
#Precio total
precio = Label(master, text="Precio", bg="#01F56A")
precio.grid(row=7, column=0, sticky="w", padx=20, pady=7)
entry_precio = Entry(master, textvariable=v_precio)
entry_precio.grid(row=7, column=1, sticky="w")

#Boton alta
boton_alta = Button(master, text="Alta", command=lambda:alta_view())
boton_alta.grid(row=8, column=1, pady=10, padx=50, ipadx=10,sticky="w")

#Sector consulta por cliente
consultar = Label(master, text="Consultar por cliente:")
consultar.grid(row=2, column=3, sticky="w")
entry_consultar = Entry(master, textvariable=v_consulta)
entry_consultar.grid(row=2, column=5, sticky="w")
boton_consultar = Button(master, text="Buscar", command=lambda:consulta_view())
boton_consultar.grid(row=2, column=4, ipadx=10)

#Sector balance total
balance = Label(master, text="Balance total:")
balance.grid(row=4, column=3, sticky="e")
entry_balance = Entry(master, textvariable=v_balance)
entry_balance.grid(row=4, column=5, sticky="w")
boton_calcular = Button(master, text="Calcular", command=lambda:balance_view())
boton_calcular.grid(row=4, column=4, ipadx=6, pady=5)

#Boton exportar
boton_exportar = Button(master, text="Exportar")
boton_exportar.grid(row=6, column=3)

#Boton cambiar color
boton_color = Button(master, text="Color fondo", command=lambda:cambiar_fondo())
boton_color.grid(row=6, column=4)

#Boton limpiar todo
boton_borrar_todo = Button(master, text="Borrar todo")
boton_borrar_todo.grid(row=6, column=5)

#Boton modificar
boton_modificar = Button(master, text="Modificar", command=lambda:modificar_view())
boton_modificar.grid(row=8, column=0, pady=10, padx=50, ipadx=10,sticky="w")

#Boton borrar
boton_borrar = Button(master, text="Borrar", command=lambda:borrar_view())
boton_borrar.grid(row=8, column=3, ipadx=10)

#Boton ver todos
boton_todos = Button(master, text="Ver todos", command=lambda:actualizar_tree(tree))
boton_todos.grid(row=8, column=5, ipadx=10, padx=30,sticky="w")

#Treeview
tree = ttk.Treeview(master, height=15)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6")
tree.column("#0", width=50, minwidth=50, anchor="w")
tree.heading("#0", text="Orden")
tree.column("col1", width=200, minwidth=200, anchor="w")
tree.heading("col1", text="Nombre")
tree.column("col2", width=120, minwidth=120, anchor="w")
tree.heading("col2", text="Telefono")
tree.column("col3", width=100, minwidth=100, anchor="w")
tree.heading("col3", text="Tipo de lavado")
tree.column("col4", width=60, minwidth=60, anchor="w")
tree.heading("col4", text="Cantidad")
tree.column("col5", width=100, minwidth=100, anchor="w")
tree.heading("col5", text="Fecha de entrega")
tree.column("col6", width=80, minwidth=60, anchor="w")
tree.heading("col6", text="Precio")

tree.grid(row=9, column=0, columnspan=6, padx=30, pady=10)


########## FUNCIONES ##########

def limpiar_entrys(): #Limpia los entrys a la hora de realizar un alta o modificacion.
    lista_entrys = [v_nombre, v_telefono, v_tipo, v_cantidad, v_fecha_entrega, v_precio]
    for var in lista_entrys:
        var.set("")

def alta_view():
    if alta_orden(v_nombre.get(),v_telefono.get(),v_tipo.get(),v_cantidad.get(),v_fecha_entrega.get(),v_precio.get(), tree) == True:
        mensaje_alta = Label(master, text="Orden generada satisfactoriamente.", fg="green")
        mensaje_alta.place(x=290, y=655)
        master.after(6000, lambda label:label.destroy(), mensaje_alta)
        limpiar_entrys()
        actualizar_tree(tree)
    else:
        mensaje_error = Label(master, text="Error! El campo 'Telefono' solo debe contenter numeros!", fg="red")
        mensaje_error.place(x=240, y=655)
        master.after(6000, lambda label:label.destroy(), mensaje_error)

def borrar_view():
    try:
        borrar_orden(tree)
        #Mensaje de evento en la ventana de Tkinter y en consola.
        mensaje_borrar = Label(master, text="Orden eliminada satisfactoriamente.", fg="blue")
        mensaje_borrar.place(x=290, y=655)
        master.after(6000, lambda label:label.destroy(), mensaje_borrar)
    except:
        print("No selecciono ningun campo para borrar!")
        mensaje_borrar = Label(master, text="No selecciono ninguna orden para borrar!", fg="black")
        mensaje_borrar.place(x=290, y=655)
        master.after(6000, lambda label:label.destroy(), mensaje_borrar)

def modificar_view():
    if modificar_orden(v_nombre.get(),v_telefono.get(),v_tipo.get(),v_cantidad.get(),v_fecha_entrega.get(),v_precio.get(),tree):
        #Mensaje de evento en la ventana de Tkinter y en consola.
        mensaje_modificacion = Label(master, text=f"Se ha modificado correctamente la orden", fg="green")
        mensaje_modificacion.place(x=240, y=655)
        master.after(6000, lambda label:label.destroy(), mensaje_modificacion)
        limpiar_entrys()
    else:
        #Mensaje de evento en la ventana de Tkinter y en consola.
        mensaje_error_modificacion = Label(master, text=f"Error! No debe haber ningun campo vacio para modificar!", fg="black")
        mensaje_error_modificacion.place(x=240, y=655)
        master.after(6000, lambda label:label.destroy(), mensaje_error_modificacion)

def consulta_view():
    if consulta_nombre(v_consulta.get(), tree):
        pass
    else:
        mensaje_vacio = Label(master, text="El campo no debe estar vacio, por favor indique el nombre del cliente.")
        mensaje_vacio.place(x=190, y=655)
        master.after(6000, lambda label:label.destroy(), mensaje_vacio)

def balance_view():
    if entry_balance == "":
        resultado = balance_total()
        entry_balance.insert(0, f'${resultado}') #Muestra el resultado en el entry
    else:
        v_balance.set("")
        resultado = balance_total()
        entry_balance.insert(0, f'${resultado}')

def cambiar_fondo(): #Funcion que cambia color de la ventana master
    color_elegido = askcolor(color="#00ff00",title="Seleccione un color" )
    master.configure(background=color_elegido[1])


actualizar_tree(tree)
master.mainloop()