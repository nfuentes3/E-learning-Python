import sqlite3
import re

class OperacionesDB:

    def __init__(self, nombre_db = "ordenes.db"):
        self.conexion = sqlite3.connect(nombre_db)
        self.cursor = self.conexion.cursor()
        self.__crear_tabla() #Llamo al metodo crear tabla para que al abrir, intente crear la tabla si no existe.

    def __crear_tabla(self): #Clase privada para la creacion de la tabla
        try:
            self.cursor.execute(
                """ CREATE TABLE IF NOT EXISTS ordenes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre varchar(20),
                telefono int,
                tipo varchar(20),
                cantidad int,
                fecha varchar(20),
                precio float
            )
            """)
            self.conexion.commit()
        except:
            print("ERROR AL CREAR TABLA EN BASE DE DATOS.")
    
    def alta_orden(self, nombre, telefono, tipo, cantidad, fecha, precio): #Alta de orden en db.
        try:
            if re.match(r"^\d", telefono):
                self.cursor.execute(
                """INSERT INTO ordenes (
                nombre,
                telefono,
                tipo,
                cantidad,
                fecha,
                precio) VALUES (?,?,?,?,?,?)""", (nombre, telefono, tipo, cantidad, fecha, precio))
                self.conexion.commit()
                print("Orden dada de alta:")
                print(f"Nombre: {nombre}\nTelefono: {telefono}\nTipo: {tipo}\nCantidad: {cantidad}\nFecha de entrega: {fecha}\nPrecio: $ {precio}\n")
                print("***"*10)
            else:
                print("El campo 'Telefono' solo debe contener numeros!")
        except:
            print("ERROR EN ALTA DE ORDEN.")
            print("***"*10)
    
    def consulta_ordenes(self): #Devuelve todas las ordenes disponibles en la db
        ordenes = self.cursor.execute("SELECT * FROM ordenes ORDER BY id ASC")
        resultado = ordenes.fetchall()
        return resultado
    
    def borrar_orden(self, id): #Borra la orden perteneciente al id
        try:
            self.cursor.execute("DELETE FROM ordenes WHERE id = ?;", id)
            self.conexion.commit()
            print(f"Se ha borrado la orden: {id}")
            print("***" * 10)
        except:
            print(f"ERROR AL BORRAR ORDEN {id} EN BASE DE DATOS ")
            print("***" * 10)
    
    def consulta_nombre(self, nombre): #Devuelve los resultados segun coincidencia en la columna 'nombre'
        try:
            if nombre != '':
                ordenes_nombre = self.cursor.execute("SELECT * FROM ordenes WHERE nombre = ? ORDER BY id ASC", (nombre,))
                resultado = ordenes_nombre.fetchall()
                print(f"Ordenes encontradas de: {nombre}")
                for fila in resultado:
                    print(fila)
                print("***" * 10)
                return resultado
            else:
                print("ERROR: El campo esta de busqueda esta vacio.")
                print("***" * 10)
        except:
            print("No se encontaron resultados.")
            print("***" * 10)

    def modificar_orden(self, id, nombre, telefono, tipo, cantidad, fecha, precio): #Modifica la orden del id seleccionado
        try:
            self.cursor.execute("UPDATE ordenes SET nombre = ?, telefono = ?, tipo = ?, cantidad = ?, fecha = ?, precio = ? WHERE id = ?", (nombre, telefono, tipo, cantidad, fecha, precio, id))
            self.conexion.commit()
            print(f"Se modifico la orden: {id}")
            print("***" * 10)
        except:
            print("ERROR: No se pudo modificar la orden (modelo).")



if __name__ == "__main__":
    db = OperacionesDB()
    db.alta_orden("Test","123123123","Completo","2","30/10",4500)
    print(db.consulta_ordenes())
    print(db.consulta_nombre("Nicolas Fuentes"))
    db.borrar_orden("9")