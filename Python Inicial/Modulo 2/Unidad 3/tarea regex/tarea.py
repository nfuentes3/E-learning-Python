from tkinter import *
from tkinter import ttk
import sqlite3
import re

master  = Tk()
master.geometry("300x400")

#Defino las variables para tkinter
var_producto = StringVar()
var_descripcion = StringVar()

###### MODELO ######
def conexion(): #Genero creación e instancia de conexión con la base.
    con = sqlite3.connect("base_productos.db")
    return con

def crear_tabla(): #Genero una función para crear la tabla con la instancia generada antes "con"
    con = conexion()
    cursor = con.cursor()
    sql = "CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY AUTOINCREMENT, producto varchar(20) NOT NULL, descripcion text)"
    cursor.execute(sql)
    con.commit()

def guardar_producto(producto, descripcion, tree): #Genero una función donde genere conexion con la tabla e inserte el registro obtenido.
    crear_tabla()
    con = conexion()
    cursor = con.cursor()
    if re.match("^[a-zA-Z0-9 ñÑ]+$",producto): #Creo un condicional con un RegEx donde solamente admita valores alfanuméricos.
            data = (producto, descripcion)
            sql = "INSERT INTO productos(producto, descripcion) VALUES (?,?)"
            cursor.execute(sql, data)
            con.commit()
            print(f"Producto dado de alta:\nProducto: {producto}\nDescripción: {descripcion}")
            actualizar_tree(tree)
    else:
        print("Error! El producto no debe estar vacío o debe contener solamente caracteres alfanuméricos.\nIngrese otro producto.")

def actualizar_tree(tree_productos): #Genero una función para actualizar los datos del Treeview de Tkinter al dar de alta un producto.
    registros = tree_productos.get_children()
    for registro in registros:
        tree_productos.delete(registro)
    
    sql = "SELECT * FROM productos ORDER BY id DESC"
    con = conexion()
    cursor = con.cursor()
    datos = cursor.execute(sql)
    
    resultado = datos.fetchall()
    for fila in resultado:
        tree_productos.insert("", 0, text=fila[0], values=(fila[1], fila[2]))

###### VISTA ######
titulo = Label(master, text="Generador de alta de productos", bg="#3284ED", fg="white") #Titulo
titulo.grid(row=0, column=0, padx=2, pady=2, columnspan=4)

label_producto = Label(master, text="Producto: ") #Producto
label_producto.grid(row=1, column=0, sticky=W)
entry_producto = Entry(master, textvariable=var_producto)
entry_producto.grid(row=1, column=1)

label_descripcion = Label(master, text="Descripcion: ") #Descripción
label_descripcion.grid(row=2, column=0, sticky=W)
entry_descripcion = Entry(master, textvariable=var_descripcion)
entry_descripcion.grid(row=2, column=1)

boton_guardar = Button(master, text="Guardar", command=lambda:guardar_producto(var_producto.get(),var_descripcion.get(), tree)) #Boton Guardar
boton_guardar.grid(row=3, column=0, padx=2, pady=2)

tree = ttk.Treeview(master) #Creacion de Treeview con sus columnas correspondientes.
tree["columns"] = ("col1", "col2")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.heading("#0", text="ID")
tree.column("col1", width=100, minwidth=100, anchor=W)
tree.heading("col1", text="Producto")
tree.column("col2", width=100, minwidth=100, anchor=W)
tree.heading("col2", text="Descripcion")
tree.grid(column=0, row=4, columnspan=4)

master.mainloop()