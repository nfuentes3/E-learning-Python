from peewee import *
import re
from datetime import datetime

# Genero instancia de la base de datos con Sqlite
db = SqliteDatabase("ordenes_lavadero.db")


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
            table_name = "ordenes"

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
    def __init__(self):
        self._observadores = []

    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def eliminar_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self, accion, datos):
        for observador in self._observadores:
            observador.update(accion, datos)

    def alta_orden(self, nombre, telefono, tipo, cantidad, fecha, horario, precio):
        try:
            self.nombre = nombre
            self.telefono = telefono
            self.tipo = tipo
            self.cantidad = cantidad
            self.fecha = fecha
            self.horario = horario
            self.precio = precio

            if not re.match(r"^\d+$", str(telefono)) or telefono == "":
                print("El campo 'Telefono' no cumple con las condiciones.")
                return False
            elif not re.match(r"^\d+$", str(precio)) or precio == "":
                print("El campo 'Precio' no cumple con las condiciones.")
                return False
            else:
                nueva_orden = Ordenes.create(
                    nombre=nombre,
                    telefono=telefono,
                    tipo=tipo,
                    cantidad=cantidad,
                    fecha=fecha,
                    horario=horario,
                    precio=precio,
                )
                return nueva_orden
        except DataError as de:
            print("Error con los datos:", de)
        except IntegrityError as ie:
            print("Error de integridad:", ie)
        except Exception as err:
            print("Ocurrio un error inesperado:", err)

    def borrar_orden(self, id):
        try:
            if not id and not isinstance(id, int):
                print(f"Error, el ID {id} es invalido.")
            else:
                self.id = id
                borrar = Ordenes.get(id)
                borrar.delete_instance()
        except DoesNotExist as ne:
            print("El ID {id} no existe:", ne)
        except Exception as err:
            print("Ocurrio un error inesperado:", err)

    def modificar_orden(
        self, id, nombre, telefono, tipo, cantidad, fecha, horario, precio
    ):
        try:
            orden = Ordenes.get_or_none(Ordenes.id == id)
            if not orden:
                print(f"El ID {id} no existe en la db")
                return False

            Ordenes.update(
                nombre=nombre,
                telefono=telefono,
                tipo=tipo,
                cantidad=cantidad,
                fecha=fecha,
                horario=horario,
                precio=precio,
            ).where(Ordenes.id == id).execute()
        except Exception as err:
            print("Ocurrio un error inesperado:", err)

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

    def exportar_ordenes(self):  # Exporta todas las ordenes de la tabla
        try:
            fecha = datetime.now().strftime("%d-%m-%Y %H_%M_%S")
            archivo = open(f"ordenes_{fecha}.txt", "w")
            ordenes = Ordenes.select().dicts()
            total = 0
            for fila in ordenes:
                archivo.write(
                    f"{fila['id']},{fila['nombre']},{fila['telefono']},{fila['tipo']},{fila['cantidad']},{fila['fecha']},{fila['horario']},{fila['precio']}\n"
                )
                total += fila["precio"]
            archivo.write(f"Total a recaudar: $ {total}")
            archivo.close()
            print(
                f"Se exporto el archivo: ordenes_{fecha}.txt con todos los registros."
            )
            print("***" * 10)
            archivo.close()
        except Exception as err:
            print("Error al exportar las ordenes:", err)


if __name__ == "__main__":
    # op = OperacionesCRUD()
    # op.alta_orden("ggggggggg","11111","secado",2,"21/11","Tarde","44123")
    # op.borrar_orden(22)
    # op.modificar_orden(6, "cdddd",1233,"completo",2,"09/11","Tarde",3400)
    # op.consulta_ordenes()
    # op.consulta_nombre("Daiana Patta")
    # op.borrar_todo()
    # op.exportar_ordenes()
    pass
