from tkinter import *
from tkinter import ttk
import sqlite3
import re
from datetime import datetime
from tkinter.colorchooser import askcolor
from tkinter import messagebox

master = Tk()
master.geometry("770x700")
master.title("Lavadero - Calle Falsa 123")
#Genero variables de tkinter
v_nombre, v_telefono, v_tipo, v_cantidad, v_precio, v_fecha_entrega, v_consulta, v_balance = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

########## MODELO ##########
def conexion(): #Creacion a la db y returna instancia de conexion.
    con = sqlite3.connect("ordenes.db")
    return con

def crear_tabla(): #Creacion de tabla.
    #Conexion y accion en db.
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

def actualizar_tree(ordenes_tree): #Actualiza y muestra todas las ordenes de la db en el treeview.
    crear_tabla()
    ordenes = ordenes_tree.get_children()
    for orden in ordenes:
        ordenes_tree.delete(orden)
    #Conexion y accion en db.
    con = conexion()
    cursor = con.cursor()
    sql = "SELECT * FROM ordenes ORDER BY id ASC"
    datos = cursor.execute(sql)
    #Inserta los datos en el treeview.
    resultados = datos.fetchall()
    for fila in resultados:
        ordenes_tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]))

def borrar_orden(tree): #Borra orden en db seleccionada del treeview.
    seleccion = tree.selection()
    orden = tree.item(seleccion)
    id_orden = orden['text']
    #Conexion y accion en db.
    con=conexion()
    cursor = con.cursor()
    data = (id_orden,)
    sql = "DELETE FROM ordenes WHERE id = ?;"
    cursor.execute(sql, data)
    con.commit()
    tree.delete(seleccion)
    #Mensaje de evento en la ventana de Tkinter y en consola.
    mensaje_borrar = Label(master, text="Orden eliminada satisfactoriamente.", fg="blue")
    mensaje_borrar.place(x=290, y=655)
    master.after(6000, borrar_mensaje, mensaje_borrar)
    print(f"Se borro la orden {id_orden} de {orden['values'][0]}")
    print("***"*10)
    #Insercion de registro en log.
    log = f"Baja = Orden: {id_orden}, Nombre: {orden['values'][0]}, Telefono: {orden['values'][1]}, Tipo: {orden['values'][2]}, Cantidad: {orden['values'][3]}, Fecha: {orden['values'][4]}, Precio: {orden['values'][5]}."
    insertar_log(log)

def modificar_orden(nombre, telefono, tipo, cantidad, fecha_entrega, precio, tree): #Modifica la orden en db seleccionada en el treeview.
    seleccion = tree.selection()
    orden = tree.item(seleccion)
    id_orden = orden['text']
    if nombre != '' and telefono != '' and tipo != '' and cantidad != '' and fecha_entrega != '' and precio != '': #Declaro una condicional de que no haya nigun campo vacio.
        #Conexion y accion en db.
        con=conexion()
        cursor = con.cursor()
        data = (nombre, telefono, tipo, cantidad, fecha_entrega, precio, id_orden)
        sql = "UPDATE ordenes SET nombre = ?, telefono = ?, tipo = ?, cantidad = ?, fecha = ?, precio = ? WHERE id = ?"
        cursor.execute(sql, data)
        con.commit()
        actualizar_tree(tree)
        #Mensaje de evento en la ventana de Tkinter y en consola.
        mensaje_modificacion = Label(master, text=f"Se ha modificado correctamente la orden: {id_orden}", fg="green")
        mensaje_modificacion.place(x=240, y=655)
        master.after(6000, borrar_mensaje, mensaje_modificacion)
        print(f"Se modificó la orden {id_orden} de {orden['values'][0]}")
        print("***"*10)
        #Insercion de registro en log.
        log = f"Modificacion = Orden: {id_orden}, Nombre: {orden['values'][0]}, Telefono: {orden['values'][1]}, Tipo: {orden['values'][2]}, Cantidad: {orden['values'][3]}, Fecha: {orden['values'][4]}, Precio: {orden['values'][5]}."
        insertar_log(log)
        #Limpieza de los entrys.
        limpiar_entrys()
    else:
        print("Error! Falta un dato para completar.")
        #Mensaje de evento en la ventana de Tkinter y en consola.
        mensaje_error_modificacion = Label(master, text=f"Error! No debe haber ningun campo vacio para modificar!", fg="black")
        mensaje_error_modificacion.place(x=240, y=655)
        master.after(6000, borrar_mensaje, mensaje_error_modificacion)

def borrar_base(tree):
    user_consulta = messagebox.askokcancel(message="Desea eliminar todos los registros?", title="Borrar todos los datos")
    if user_consulta == True:
        #Conexion y accion en db.
        con = conexion()
        cursor = con.cursor()
        sql = "DELETE FROM ordenes"
        cursor.execute(sql)
        con.commit()
        #Mensaje de evento en la ventana de Tkinter y en consola.
        mensaje_borrar_base = Label(master, text=f"Se han eliminado todos los registros.", fg="blue")
        mensaje_borrar_base.place(x=280, y=655)
        master.after(6000, borrar_mensaje, mensaje_borrar_base)
        print("Se eliminaron todos los registros de la tabla 'Ordenes'.")
        print("***"*10)
        
        actualizar_tree(tree)
    else:
        print("Operacion cancelada (borrar todos los registros.)")
        mensaje_borrar_base = Label(master, text=f"Operacion anulada.", fg="black")
        mensaje_borrar_base.place(x=320, y=655)
        master.after(6000, borrar_mensaje, mensaje_borrar_base)

########## VISTA ##########
#Encabezado
encabezado = Label(master, text="Gestor de ordenes", bg="#2664FA", fg="white")
encabezado.grid(row=0, column=0, columnspan=8, sticky=W+E)
#Fecha y hora
fecha = datetime.now()
fecha_format_pantalla = fecha.strftime("%d/%m/%Y    %H:%M")
fecha_label = Label(master, text=f"{fecha_format_pantalla}")
fecha_label.grid(row=1, column=4, sticky=W ,padx=20)
#Seccion alta
titulo_alta = Label(master, text="Generar o modificar orden:")
titulo_alta.grid(row=1, column=0, sticky=W ,padx=20)
#Nombre
nombre = Label(master, text="Nombre", bg="#01F56A")
nombre.grid(row=2, column=0,sticky=W, padx=20, pady=7)
entry_nombre = Entry(master, textvariable=v_nombre)
entry_nombre.grid(row=2, column=1,sticky=W)
#Telefono
telefono = Label(master, text="Telefono", bg="#01F56A")
telefono.grid(row=3, column=0, sticky=W, padx=20, pady=7)
entry_telefono = Entry(master, textvariable=v_telefono)
entry_telefono.grid(row=3, column=1, sticky=W)
#Tipo de lavado
tipo = Label(master, text="Tipo de lavado", bg="#01F56A")
tipo.grid(row=4, column=0, sticky=W, padx=20, pady=7)
entry_tipo = Entry(master, textvariable=v_tipo)
entry_tipo.grid(row=4, column=1, sticky=W)
#Cantidad de valet
cantidad = Label(master, text="Cantidad", bg="#01F56A")
cantidad.grid(row=5, column=0, sticky=W, padx=20, pady=7)
entry_cantidad = Entry(master, textvariable=v_cantidad)
entry_cantidad.grid(row=5, column=1, sticky=W)
#Fecha de entrega
fecha_entrega = Label(master, text="Fecha de entrega", bg="#01F56A")
fecha_entrega.grid(row=6, column=0, sticky=W, padx=20, pady=7)
entry_fecha_entrega = Entry(master, textvariable=v_fecha_entrega)
entry_fecha_entrega.grid(row=6, column=1, sticky=W)
#Precio total
precio = Label(master, text="Precio", bg="#01F56A")
precio.grid(row=7, column=0, sticky=W, padx=20, pady=7)
entry_precio = Entry(master, textvariable=v_precio)
entry_precio.grid(row=7, column=1, sticky=W)

#Boton alta
boton_alta = Button(master, text="Alta", command=lambda:alta_orden(v_nombre.get(),v_telefono.get(),v_tipo.get(),v_cantidad.get(),v_fecha_entrega.get(),v_precio.get(),tree))
boton_alta.grid(row=8, column=1, pady=10, padx=50, ipadx=10,sticky=W)

#Sector consulta por cliente
consultar = Label(master, text="Consultar por cliente:")
consultar.grid(row=2, column=3, sticky=W)
entry_consultar = Entry(master, textvariable=v_consulta)
entry_consultar.grid(row=2, column=5, sticky=W)
boton_consultar = Button(master, text="Buscar", command=lambda:consulta_nombre(v_consulta.get(),tree))
boton_consultar.grid(row=2, column=4, ipadx=10)

#Sector balance total
balance = Label(master, text="Balance total:")
balance.grid(row=4, column=3, sticky=E)
entry_balance = Entry(master, textvariable=v_balance)
entry_balance.grid(row=4, column=5, sticky=W)
boton_calcular = Button(master, text="Calcular", command=lambda:balance_total())
boton_calcular.grid(row=4, column=4, ipadx=6, pady=5)

#Boton exportar
boton_exportar = Button(master, text="Exportar", command=lambda:exportar_ordenes())
boton_exportar.grid(row=6, column=3)

#Boton cambiar color
boton_color = Button(master, text="Color fondo", command=lambda:cambiar_fondo())
boton_color.grid(row=6, column=4)

#Boton limpiar todo
boton_borrar_todo = Button(master, text="Borrar todo", command=lambda:borrar_base(tree))
boton_borrar_todo.grid(row=6, column=5)

#Boton modificar
boton_modificar = Button(master, text="Modificar", command=lambda:modificar_orden(v_nombre.get(),v_telefono.get(),v_tipo.get(),v_cantidad.get(),v_fecha_entrega.get(),v_precio.get(),tree))
boton_modificar.grid(row=8, column=0, pady=10, padx=50, ipadx=10,sticky=W)

#Boton borrar
boton_borrar = Button(master, text="Borrar", command=lambda:borrar_orden(tree))
boton_borrar.grid(row=8, column=3, ipadx=10)

#Boton ver todos
boton_todos = Button(master, text="Ver todos", command=lambda:actualizar_tree(tree))
boton_todos.grid(row=8, column=5, ipadx=10, padx=30,sticky=W)

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

def alta_orden(nombre, telefono, tipo, cantidad, fecha_entrega, precio, tree): #Crea una orden y actualiza el treeview con todas las ordenes.
    crear_tabla()
    con = conexion()
    cursor = con.cursor()
    #Inserta una nueva orden con los argumentos obtenidos de los entrys.
    if re.match(r"^\d", telefono): #Se utiliza RegEx para que solo tome numeros como valores.
        data = (nombre, telefono, tipo, cantidad, fecha_entrega, precio)
        sql = """INSERT INTO ordenes (
            nombre,
            telefono,
            tipo,
            cantidad,
            fecha,
            precio) VALUES (?,?,?,?,?,?)"""
        #Conexion y accion en db.
        cursor.execute(sql, data)
        con.commit()
        orden_id = cursor.lastrowid
        #Mensaje de evento en la ventana de Tkinter y en consola.
        print("Orden dada de alta:")
        print(f"Nombre: {nombre}\nTelefono: {telefono}\nTipo: {tipo}\nCantidad: {cantidad}\nFecha de entrega: {fecha_entrega}\nPrecio: {precio}\n")
        print("***"*10)
        mensaje_alta = Label(master, text="Orden generada satisfactoriamente.", fg="green")
        mensaje_alta.place(x=290, y=655)
        master.after(6000, borrar_mensaje, mensaje_alta)
        #Insercion de registro en log.
        log = f"Alta = Orden: {orden_id}, Nombre: {nombre}, Telefono: {telefono}, Tipo: {tipo}, Cantidad: {cantidad}, Fecha: {fecha_entrega}, Precio: {precio}."
        insertar_log(log)
        #Limpieza de los entrys.
        limpiar_entrys()
        
        actualizar_tree(tree)
    else:
        mensaje_error = Label(master, text="Error! El campo 'Telefono' solo debe contenter numeros!", fg="red")
        mensaje_error.place(x=240, y=655)
        master.after(6000, borrar_mensaje, mensaje_error)

def consulta_nombre(nombre,tree): #Busca el nombre del cliente y muestra en el treeview sus ordenes vigentes (Busqueda exacta).
    if nombre != '': #Condicional para que el campo no este vacio.
        ordenes = tree.get_children()
        for orden in ordenes:
            tree.delete(orden)
        #Conexion y accion en db.
        con = conexion()
        cursor = con.cursor()
        data = (nombre,)
        sql = "SELECT * FROM ordenes WHERE nombre = ? ORDER BY id ASC"
        datos = cursor.execute(sql,data,)
        #Inserta los resultados en el treeview.
        resultados = datos.fetchall()
        for fila in resultados:
            tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]))
    else:
        mensaje_vacio = Label(master, text="El campo no debe estar vacio, por favor indique el nombre del cliente.")
        mensaje_vacio.place(x=190, y=655)
        master.after(6000, borrar_mensaje, mensaje_vacio)

def balance_total(): #Calcula el balance total de todos los precios.
    precio_total = 0
    #Conexion y accion en db.
    con = conexion()
    cursor = con.cursor()
    sql = "SELECT * FROM ordenes ORDER BY id ASC"
    datos = cursor.execute(sql)
    #Inserta los datos en el treeview.
    resultados = datos.fetchall()
    for fila in resultados: #Itera cada reigstro, busca el precio y lo suma, para insertarlo en el entry.
        precio_total += fila[6]
    print(f'El balance total es de ${precio_total}')
    print("***"*10)
    entry_balance.insert(0, f'${precio_total}') #Muestra el resultado en el entry

def borrar_mensaje(label): #Borra los label informativos que salen en la perte inferior de la app.
    label.destroy()

def limpiar_entrys(): #Limpia los entrys a la hora de realizar un alta o modificacion.
    lista_entrys = [v_nombre, v_telefono, v_tipo, v_cantidad, v_fecha_entrega, v_precio]
    for var in lista_entrys:
        var.set("")

def insertar_log(registro_log): #Inserta registros en un .txt de Alta, Baja y Modificacion.
    log = open("log.txt", "a")
    log.write(f'{registro_log}\n')

def exportar_ordenes(): #Exoporta todos los registros de la db en un .txt
    fecha_format_txt = fecha.strftime("%d-%m-%Y_%H%M%S")
    ordenes_actuales = open(f"ordenes_{fecha_format_txt}.txt","w") #Coloca como titulo la fecha y hora de ejecucion.
    #Conexion y accion en db.
    con = conexion()
    cursor = con.cursor()
    sql = "SELECT * FROM ordenes ORDER BY id ASC"
    datos = cursor.execute(sql)
    resultados = datos.fetchall()
    precio_total = 0
    #Escribe cada resultado en el .txt
    for fila in resultados:
        ordenes_actuales.write(f"Orden:{fila[0]}, Nombe: {fila[1]}, Telefono:{fila[2]}, Tipo: {fila[3]}, Cantidad: {fila[4]}, Fecha de entrega: {fila[5]}, Precio: {fila[6]} \n")
        precio_total += fila[6]
    ordenes_actuales.write(f"Total a recaudar: $ {precio_total}")
    #Mensaje de evento en la ventana de Tkinter y en consola.
    print(f"Se exporto el archivo: {fecha_format_txt}.txt con todos los registros.")
    print("***"*10)
    ordenes_actuales.close()
    mensaje_exportado = Label(master, text="Se exporto el archivo con todas las ordenes vigentes.")
    mensaje_exportado.place(x=240, y=655)
    master.after(6000, borrar_mensaje, mensaje_exportado)

def cambiar_fondo(): #Funcion que cambia color de la ventana master
    color_elegido = askcolor(color="#00ff00",title="Seleccione un color" )
    master.configure(background=color_elegido[1])

actualizar_tree(tree) #Se llama a esta funcion para al abrir la app, muestre todos los registros de la db.
master.mainloop()