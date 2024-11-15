from peewee import *
import re
from datetime import datetime

#Creacion de archivo modelo con uso de ORM Peewee

db = SqliteDatabase('ordenes_orm.db')

class BaseModel(Model):
    class Meta:
        database = db

class Ordenes(BaseModel): #Creacion de la tabla en la base de datos
    nombre = CharField()
    telefono = IntegerField()
    tipo = CharField()
    cantidad = IntegerField()
    fecha = CharField()
    horario = CharField()
    precio = IntegerField()
    
    class Meta:
        table_name = "ordenesORM"

    def _crear_tabla(self): #Metodo para la creacion de la tabla
        try:
            db.connect()
            db.create_tables([Ordenes])
            print("***"*10)
            print("Conexion OK y tablas creadas")
            print("***"*10)
        except:
            print("Error en la conexion a la DB")


class OperacionesDB: #Clase para operaciones de la base de datos
    def __init__(self):
        self.db = Ordenes()



    def alta_orden(self, nombre, telefono, tipo, cantidad, fecha, horario, precio): #Generar una nueva orden en la tabla
        self.db = Ordenes()
        self.db.nombre = nombre
        self.db.telefono = telefono
        self.db.tipo = tipo
        self.db.cantidad = cantidad
        self.db.fecha = fecha
        self.db.horario = horario
        self.db.precio = precio
        try:
            if not re.match(r'^\d+$', str(telefono)) or telefono == '':
                print("El campo 'Telefono' solo debe contener numeros ni debe estar vacio!")
                return False
            elif not re.match(r'^\d+$', str(precio)) or precio == "":
                print("El campo 'Precio' solo debe contener numeros ni debe estar vacio!")
                return False
            else:
                self.db.save()
                print("Orden dada de alta:")
                print(f"Nombre: {nombre}\nTelefono: {telefono}\nTipo: {tipo}\nCantidad: {cantidad}\nFecha de entrega: {fecha}\nHorario: {horario}\nPrecio: $ {precio}\n")
                print("***"*10)
                return True
        except:
            print("Error de alta en la DB")

    def borrar_orden(self, id): #Borra una orden en la tabla
        self.id = id
        borrar = Ordenes.get(id)
        try:
            borrar.delete_instance()
            print(f"Se ha borrado la orden: {id}")
            print("***" * 10)
        except:
            print(f"ERROR AL BORRAR ORDEN {id} EN BASE DE DATOS ")
            print("***" * 10)

    def modificar_orden(self, id, nombre, telefono, tipo, cantidad, fecha, horario, precio): #Modifica una orden en la tabla
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.tipo = tipo
        self.cantidad = cantidad
        self.fecha = fecha
        self.horario = horario
        self.precio = precio
        
        try:
            self.modificar = Ordenes.update(nombre=self.nombre, telefono=self.telefono, tipo=self.tipo, cantidad=self.cantidad, fecha=self.fecha, horario=self.horario, precio=self.precio).where(Ordenes.id == self.id)
            self.modificar.execute()
            print(f"Se modifico la orden: {id}")
            print("***" * 10)
        except:
            print("ERROR: No se pudo modificar la orden (modelo).")

    def consulta_ordenes(self): #Devuelve todos los registros de la tabla
        todos = Ordenes.select().dicts()
        return todos

    def consulta_nombre(self, persona): #Devuelve todos los registros de la tabla que tengan el nombre de persona
        try:
            if persona != '':
                consulta = Ordenes.select().where(Ordenes.nombre == persona).dicts()
                print(f"Ordenes encontradas de {persona}:", len(consulta))
                for orden in consulta:
                    print(orden)
                return consulta
            else:
                print("ERROR! El campo nombre no puede estar vacio")
        except:
            print("No se encontaron resultados.")
            print("***" * 10)

    def borrar_todo(self): #Borra todas las ordenes de la tabla
        try:
            Ordenes.delete().execute()
            print("Borrado OK en la DB")
        except:
            print("Error al borrar la tabla")
    
    def exportar_ordenes(self): #Exporta todas las ordenes de la tabla
        try:
            fecha = datetime.now().strftime("%d-%m-%Y %HH-%MM-%SS")
            archivo = open(f"ordenes_{fecha}.txt", "w")
            ordenes = Ordenes.select().dicts()
            total = 0
            for fila in ordenes:
                archivo.write(f"{fila['id']},{fila['nombre']},{fila['telefono']},{fila['tipo']},{fila['cantidad']},{fila['fecha']},{fila['horario']},{fila['precio']}\n")
                total += fila['precio']
            archivo.write(f"Total a recaudar: $ {total}")
            archivo.close()
            print(f"Se exporto el archivo: {fecha}.txt con todos los registros.")
            print("***"*10)
            archivo.close()
        except:
            print("Error al exportar las ordenes.")


if __name__ == "__main__":
    #op = OperacionesDB()
    #op.alta_orden('Pepe', 123456789, 'Pequeña', 1, '2023-01-01', '12:00', 100)
    #op.alta_orden('Jorge', 123456789, 'Grande', 1, '2023-01-01', '12:00', 1200)
    #op.borrar_orden(2)
    #op.modificar_orden(3, 'ffffffff', 123456789, 'Grande', 1, '2023-01-01', '12:00', 1200)
    #op.consulta_nombre('Jorge')
    #op.borrar_todo()
    pass