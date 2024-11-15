import sqlite3
import re

########## MODELO ##########
def conexion(): #Creacion a la db y returna instancia de conexion.
    con = sqlite3.connect("ordenes.db")
    return con

def crear_tabla(): #Creacion de tabla.
    #Conexion y accion en db.
    try:
        con = conexion()
        cursor = con.cursor()
        sql = """ CREATE TABLE ordenes (
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
    except:
        print("Ya esta creada la base de datos.")

def alta_orden(nombre, telefono, tipo, cantidad, fecha_entrega, precio, tree): #Crea una orden y actualiza el treeview con todas las ordenes.
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
        #Mensaje de evento en la consola.
        print("Orden dada de alta:")
        print(f"Nombre: {nombre}\nTelefono: {telefono}\nTipo: {tipo}\nCantidad: {cantidad}\nFecha de entrega: {fecha_entrega}\nPrecio: $ {precio}\n")
        print("***"*10)
        return True
    else:
        print("Error! El campo 'Telefono' solamente debe contener numeros.")
        return False

def actualizar_tree(ordenes_tree): #Actualiza y muestra todas las ordenes de la db en el treeview.
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

def borrar_orden(tree):
    #Borra orden en db seleccionada del treeview.
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
    print(f"Se borro la orden {id_orden} de {orden['values'][0]}")
    print("***"*10)

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
        print(f"Se modificó la orden {id_orden} de {orden['values'][0]}")
        print("***"*10)
        return True
    else:
        print("Error! Falta un dato para completar.")
        return False

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
        return True
    else:
        print("Error! El campo no debe de estar vacio!")
        return False

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
    return precio_total