import sqlite3
import re
from datetime import datetime

class OperacionesDB:

    def __init__(self, nombre_db = "ordenes.db"):
        self.conexion = sqlite3.connect(nombre_db)
        self.cursor = self.conexion.cursor()
        self._crear_tabla() #Llamo al metodo crear tabla para que al abrir, intente crear la tabla si no existe.

    def _crear_tabla(self): #Clase privada para la creacion de la tabla
        try:
            self.cursor.execute(
                """ CREATE TABLE IF NOT EXISTS ordenes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre varchar(20),
                telefono int,
                tipo varchar(20),
                cantidad int,
                fecha varchar(20),
                horario varchar(20),
                precio float
            )
            """)
            self.conexion.commit()
        except:
            print("ERROR AL CREAR TABLA EN BASE DE DATOS.")
    
    def alta_orden(self, nombre, telefono, tipo, cantidad, fecha, horario, precio): #Alta de orden en db.
        try:
            if not re.match(r'^\d+$', str(telefono)) or telefono == '':
                print("El campo 'Telefono' solo debe contener numeros ni debe estar vacio!")
                return False
            elif not re.match(r'^\d+$', str(precio)) or precio == "":
                print("El campo 'Precio' solo debe contener numeros ni debe estar vacio!")
                return False
            else:
                self.cursor.execute(
                """INSERT INTO ordenes (
                nombre,
                telefono,
                tipo,
                cantidad,
                fecha,
                horario,
                precio) VALUES (?,?,?,?,?,?,?)""", (nombre, telefono, tipo, cantidad, fecha, horario, precio))
                self.conexion.commit()
                print("Orden dada de alta:")
                print(f"Nombre: {nombre}\nTelefono: {telefono}\nTipo: {tipo}\nCantidad: {cantidad}\nFecha de entrega: {fecha}\nHorario: {horario}\nPrecio: $ {precio}\n")
                print("***"*10)
                return True
        except:
            print("Error de alta en base!")

    
    def consulta_ordenes(self): #Devuelve todas las ordenes disponibles en la db
        ordenes = self.cursor.execute("SELECT * FROM ordenes ORDER BY id ASC")
        resultado = ordenes.fetchall()
        return resultado
    
    def borrar_orden(self, id): #Borra la orden perteneciente al id
        try:
            self.cursor.execute("DELETE FROM ordenes WHERE id = ?;", (id,))
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

    def modificar_orden(self, id, nombre, telefono, tipo, cantidad, fecha, horario, precio): #Modifica la orden del id seleccionado
        try:
            self.cursor.execute("UPDATE ordenes SET nombre = ?, telefono = ?, tipo = ?, cantidad = ?, fecha = ?, horario = ?, precio = ? WHERE id = ?", (nombre, telefono, tipo, cantidad, fecha, horario, precio, id))
            self.conexion.commit()
            print(f"Se modifico la orden: {id}")
            print("***" * 10)
        except:
            print("ERROR: No se pudo modificar la orden (modelo).")

    def borrar_todo(self):
        try:
            self.cursor.execute("DELETE FROM ordenes;")
            self.conexion.commit()
            print("Se han borrado todas las ordenes de la db.")
        except:
            print("Error al borrar todas las ordenes de la db.")

    def exportar_ordenes(self):
        fecha = datetime.now()
        fecha_format = fecha.strftime("%d-%m-%Y_%H-%M")
        archivo = open(f"ordenes_{fecha_format}.txt", "w")
        ordenes = self.consulta_ordenes()
        total = 0
        for orden in ordenes:
            archivo.write(f"Orden:{orden[0]}, Nombe: {orden[1]}, Telefono:{orden[2]}, Tipo: {orden[3]}, Cantidad: {orden[4]}, Fecha de entrega: {orden[5]}, Horario: {orden[6]}, Precio: {orden[7]} \n")
            total += orden[7]
        archivo.write(f"Total a recaudar: $ {total}")
        print(f"Se exporto el archivo: {fecha_format}.txt con todos los registros.")
        print("***"*10)
        archivo.close()

if __name__ == "__main__":
    db = OperacionesDB()
    #db.alta_orden("test","asdads","Completo",2,"12312","tarde","123123")
    #db.borrar_orden(3)
    #db.consulta_nombre("Nicolas Fuentes")
    #db.modificar_orden(21,"Carlos Lampe","1122312312","Completo","2","31/10/2024","Tarde",4500)
    #db.exportar_ordenes()