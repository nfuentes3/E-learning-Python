from peewee import *
import re
from datetime import datetime

#Genero instancia de la base de datos con Sqlite
db = SqliteDatabase('ordenes_lavadero.db')

def decorador_log(funcion):
    try:
        archivo_log = open("log.txt", "a")
        def envoltura(*args, **kwargs):
            resultado = funcion(*args, **kwargs)
            if resultado:
                if funcion.__name__ == "alta_orden":
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), f"- Se ha creado una nueva orden: {args[1:]}")
                    archivo_log.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Se ha creado una nueva orden: {args[1:]}\n")
                elif funcion.__name__ == "borrar_orden":
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), f"- Se ha borrado la orden: {args[1]}")
                    archivo_log.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Se ha borrado la orden: {args[1]}\n")
                elif funcion.__name__ == "modificar_orden":
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), f"- Se ha modificado la orden: {args[1:]}")
                    archivo_log.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Se ha modificado la orden: {args[1:]}\n")
            else:
                print("Error en el decorador.")
            return resultado
        return envoltura
    except Exception as err:
        print(err)


class BaseModel(Model):
    class Meta:
        database = db

class Ordenes(BaseModel):
    try:
        nombre = CharField()
        telefono = CharField()
        tipo = CharField()
        cantidad = IntegerField()
        fecha = CharField()
        horario = CharField()
        precio = IntegerField()
        
        class Meta:
            table_name = 'ordenes'

    except DatabaseError as dbe:
        print("Error en base de datos:", dbe)
    except Exception as err:
            print("Ocurrio un error inesperado:", err)

class OperacionesDB:
    def __init__(self):
        try:
            db.create_tables([Ordenes])
            print("Conexion con base de datos OK\nTablas creadas OK")
        except DatabaseError as dbe:
            print("Error en la base de datos:", dbe)
        except Exception as err:
            print("Ocurrio un error inesperado:", err)


class OperacionesCRUD:
    @decorador_log
    def alta_orden(self, nombre, telefono, tipo, cantidad, fecha, horario, precio):
        try:
            self.nombre = nombre
            self.telefono = telefono
            self.tipo = tipo
            self.cantidad = cantidad
            self.fecha = fecha
            self.horario = horario
            self.precio = precio
            
            if not re.match(r'^\d+$', str(telefono)) or telefono == '':
                print("El campo 'Telefono' no cumple con las condiciones.")
                return False
            elif not re.match(r'^\d+$', str(precio)) or precio == "":
                print("El campo 'Precio' no cumple con las condiciones.")
                return False
            else:
                nueva_orden = Ordenes.create(
                    nombre = nombre,
                    telefono = telefono,
                    tipo = tipo,
                    cantidad = cantidad,
                    fecha = fecha,
                    horario = horario,
                    precio = precio
                    )
                return True, nueva_orden
        except DataError as de:
            print("Error con los datos:", de)
        except IntegrityError as ie:
            print("Error de integridad:", ie)
        except Exception as err:
            print("Ocurrio un error inesperado:", err)

    @decorador_log
    def borrar_orden(self, id):
        try:
            if not id and not isinstance(id, int):
                print(f"Error, el ID {id} es invalido.")
            else:
                self.id = id
                borrar = Ordenes.get(id)
                borrar.delete_instance()
                return True
        except DoesNotExist:
            print("El ID {id} no existe:")
            return False
        except Exception as err:
            print("Ocurrio un error inesperado:", err)
            return False

    @decorador_log
    def modificar_orden(self, id, nombre, telefono, tipo, cantidad, fecha, horario, precio):
        try:
            orden = Ordenes.get_or_none(Ordenes.id == id)
            if not orden:
                print(f"El ID {id} no existe en la db")
                return False
            
            Ordenes.update(
                nombre = nombre,
                telefono = telefono,
                tipo = tipo,
                cantidad = cantidad,
                fecha = fecha,
                horario = horario,
                precio = precio
            ).where(Ordenes.id == id).execute()
            return True
        except Exception as err:
            print("Ocurrio un error inesperado:", err)
            return False

    def consulta_ordenes(self):
        resultado = Ordenes.select().dicts()
        return resultado

    def consulta_nombre(self, persona):
        try:
            consulta = Ordenes.select().where(Ordenes.nombre == persona).dicts()
            if persona == "":
                print("El campo 'nombre' se encuentra vacio.")
                return consulta
            elif len(consulta) == 0:
                print(f"No se encontraron ordenes de: {persona}")
                return consulta
            else:
                print(f"Ordenes encontradas de {persona}:", len(consulta))
                for orden in consulta:
                    print(orden)
                return consulta
        except DoesNotExist as ne:
            print("El ID no existe:", ne)
        except Exception as err:
            print("Ocurrio un error inesperado:", err)

    def borrar_todo(self):
        try:
            Ordenes.delete().execute()
            print("Todos los registros fueron borrados de la base de datos.")
        except Exception as err:
            print("Ocurrio un error inesperado", err)


    def exportar_ordenes(self): #Exporta todas las ordenes de la tabla
        try:
            fecha = datetime.now().strftime("%d-%m-%Y %H_%M_%S")
            archivo = open(f"ordenes_{fecha}.txt", "w")
            ordenes = Ordenes.select().dicts()
            total = 0
            for fila in ordenes:
                archivo.write(f"{fila['id']},{fila['nombre']},{fila['telefono']},{fila['tipo']},{fila['cantidad']},{fila['fecha']},{fila['horario']},{fila['precio']}\n")
                total += fila['precio']
            archivo.write(f"Total a recaudar: $ {total}")
            archivo.close()
            print(f"Se exporto el archivo: ordenes_{fecha}.txt con todos los registros.")
            print("***"*10)
            archivo.close()
        except Exception as err:
            print("Error al exportar las ordenes:", err)


if __name__ == "__main__":
    #op = OperacionesCRUD()
    #op.alta_orden("ggggggggg","123123","secado",2,"21/11","Tarde","44123")
    #op.borrar_orden(43)
    #op.modificar_orden(44, "cdddd",1233,"completo",2,"09/11","Tarde",3400)
    #op.consulta_ordenes()
    #op.consulta_nombre("Daiana Patta")
    #op.borrar_todo()
    #op.exportar_ordenes()
    pass