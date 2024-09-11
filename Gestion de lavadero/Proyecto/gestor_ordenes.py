from tkinter import *
from tkinter import ttk
import sqlite3
import re

master = Tk()
master.geometry("770x600")
master.title("Lavadero - Calle Falsa 123")
#Genero variables de tkinter
v_nombre, v_telefono, v_tipo, v_cantidad, v_precio, v_fecha_entrega, v_consulta = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

########## MODELO ##########
def conexion():
    con = sqlite3.connect("ordenes.db")
    return con

def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    sql = """ CREATE TABLE IF NOT EXISTS ordenes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre varchar(20),
        telefono int,
        tipo varchar(20),
        cantidad int,
        fecha varchar(20),
        precio float
    )
    """
    cursor.execute(sql)
    con.commit()

def actualizar_tree(ordenes_tree):
    crear_tabla()
    ordenes = ordenes_tree.get_children()
    for orden in ordenes:
        ordenes_tree.delete(orden)
    con = conexion()
    cursor = con.cursor()
    sql = "SELECT * FROM ordenes ORDER BY id ASC"
    datos = cursor.execute(sql)
    
    resultados = datos.fetchall()
    for fila in resultados:
        ordenes_tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]))

def borrar_orden(tree):
    seleccion = tree.selection()
    orden = tree.item(seleccion)
    id_orden = orden['text']

    con=conexion()
    cursor = con.cursor()
    data = (id_orden,)
    sql = "DELETE FROM ordenes WHERE id = ?;"
    cursor.execute(sql, data)
    con.commit()
    tree.delete(seleccion)
    mensaje_borrar = Label(master, text="Orden eliminada satisfactoriamente.", fg="blue")
    mensaje_borrar.place(x=290, y=565)
    master.after(6000, borrar_mensaje, mensaje_borrar)
    print(f"Se borro la orden {id_orden} de {orden['values'][0]}")

print(v_nombre.get())
########## VISTA ##########
#Encabezado
encabezado = Label(master, text="Gestor de ordenes", bg="#2664FA", fg="white")
encabezado.grid(row=0, column=0, columnspan=8, sticky=W+E)
#Seccion alta
titulo_alta = Label(master, text="Generar o modificar orden:")
titulo_alta.grid(row=1, column=0, sticky=W ,padx=20)
#Nombre
nombre = Label(master, text="Nombre", bg="#01F56A")
nombre.grid(row=2, column=0,sticky=W, padx=20)
entry_nombre = Entry(master, textvariable=v_nombre)
entry_nombre.grid(row=2, column=1,sticky=W)
#Telefono
telefono = Label(master, text="Telefono", bg="#01F56A")
telefono.grid(row=3, column=0, sticky=W, padx=20)
entry_telefono = Entry(master, textvariable=v_telefono)
entry_telefono.grid(row=3, column=1, sticky=W)
#Tipo de lavado
tipo = Label(master, text="Tipo de lavado", bg="#01F56A")
tipo.grid(row=4, column=0, sticky=W, padx=20)
entry_tipo = Entry(master, textvariable=v_tipo)
entry_tipo.grid(row=4, column=1, sticky=W)
#Cantidad de valet
cantidad = Label(master, text="Cantidad", bg="#01F56A")
cantidad.grid(row=5, column=0, sticky=W, padx=20)
entry_cantidad = Entry(master, textvariable=v_cantidad)
entry_cantidad.grid(row=5, column=1, sticky=W)
#Fecha de entrega
fecha_entrega = Label(master, text="Fecha de entrega", bg="#01F56A")
fecha_entrega.grid(row=6, column=0, sticky=W, padx=20)
entry_fecha_entrega = Entry(master, textvariable=v_fecha_entrega)
entry_fecha_entrega.grid(row=6, column=1, sticky=W)
#Precio total
precio = Label(master, text="Precio", bg="#01F56A")
precio.grid(row=7, column=0, sticky=W, padx=20)
entry_precio = Entry(master, textvariable=v_precio)
entry_precio.grid(row=7, column=1, sticky=W)

#Boton alta
boton_alta = Button(master, text="Alta", command=lambda:alta_orden(v_nombre.get(),v_telefono.get(),v_tipo.get(),v_cantidad.get(),v_fecha_entrega.get(),v_precio.get(),tree))
boton_alta.grid(row=8, column=1, pady=10, padx=50, ipadx=10,sticky=W)

#Sector consulta por cliente
consultar = Label(master, text="Consultar por cliente:")
consultar.grid(row=2, column=3, sticky=W)
entry_consultar = Entry(master, textvariable=v_consulta)
entry_consultar.grid(row=2, column=4)
boton_consultar = Button(master, text="Buscar", command=lambda:consulta_nombre(v_consulta.get(),tree))
boton_consultar.grid(row=2, column=5, ipadx=10, sticky=W)

#Boton modificar
boton_modificar = Button(master, text="Modificar")
boton_modificar.grid(row=8, column=0, pady=10, padx=50, ipadx=10,sticky=W)

#Boton borrar
boton_borrar = Button(master, text="Borrar", command=lambda:borrar_orden(tree))
boton_borrar.grid(row=8, column=3, ipadx=10)

#Boton ver todos
boton_todos = Button(master, text="Ver todos", command=lambda:actualizar_tree(tree))
boton_todos.grid(row=8, column=4, ipadx=10, padx=50)

#Treeview
tree = ttk.Treeview(master, height=15)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.heading("#0", text="Orden")
tree.column("col1", width=200, minwidth=200, anchor=W)
tree.heading("col1", text="Nombre")
tree.column("col2", width=120, minwidth=120, anchor=W)
tree.heading("col2", text="Telefono")
tree.column("col3", width=100, minwidth=100, anchor=W)
tree.heading("col3", text="Tipo de lavado")
tree.column("col4", width=60, minwidth=60, anchor=W)
tree.heading("col4", text="Cantidad")
tree.column("col5", width=100, minwidth=100, anchor=W)
tree.heading("col5", text="Fecha de entrega")
tree.column("col6", width=80, minwidth=60, anchor=W)
tree.heading("col6", text="Precio")

tree.grid(row=9, column=0, columnspan=6, padx=30, pady=10)

########## CONTROLADOR ##########

def alta_orden(nombre, telefono, tipo, cantidad, fecha_entrega, precio, tree):
    crear_tabla()
    con = conexion()
    cursor = con.cursor()
    if re.match(r"^\d", telefono):
        data = (nombre, telefono, tipo, cantidad, fecha_entrega, precio)
        sql = """INSERT INTO ordenes (
            nombre,
            telefono,
            tipo,
            cantidad,
            fecha,
            precio) VALUES (?,?,?,?,?,?)"""
        cursor.execute(sql, data)
        con.commit()
        print("Orden dada de alta:")
        print(f"Nombre: {nombre}\nTelefono: {telefono}\nTipo: {tipo}\nCantidad: {cantidad}\nFecha de entrega: {fecha_entrega}\nPrecio: {precio}\n")
        print("***"*10)
        actualizar_tree(tree)
        mensaje_alta = Label(master, text="Orden generada satisfactoriamente.", fg="green")
        mensaje_alta.place(x=290, y=565)
        master.after(6000, borrar_mensaje, mensaje_alta)
    else:
        mensaje_error = Label(master, text="Error! El campo 'Telefono' solo debe contenter numeros!", fg="red")
        mensaje_error.place(x=240, y=565)
        master.after(6000, borrar_mensaje, mensaje_error)

def consulta_nombre(nombre,tree):
    if nombre != '':
        ordenes = tree.get_children()
        for orden in ordenes:
            tree.delete(orden)
        con = conexion()
        cursor = con.cursor()
        data = (nombre,)
        sql = "SELECT * FROM ordenes WHERE nombre = ? ORDER BY id ASC"
        datos = cursor.execute(sql,data,)
    
        resultados = datos.fetchall()
        for fila in resultados:
            tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]))
    else:
        mensaje_vacio = Label(master, text="El campo no debe estar vacio, por favor indique el nombre del cliente.")
        mensaje_vacio.place(x=190, y=565)
        master.after(6000, borrar_mensaje, mensaje_vacio)

def borrar_mensaje(label):
    label.destroy()

actualizar_tree(tree)
master.mainloop()