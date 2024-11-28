Modelo
=============

Introducción
--------------
Es un modulo que interactúa con la base de datos
para realizar operaciones CRUD (Create, Read, Update, Delete)

Utiliza la librería peewee para interactuar con la base de datos
con base de datos SQLite3.

**Importaciones requeridas:**

.. code-block:: python
   
   # Librerias de terceros
   from peewee import Model, SqliteDatabase, CharField, IntegerField, DatabaseError, DataError, IntegrityError, DoesNotExist
   # Librerias de Python
   from datetime import datetime
   import re


Primero instancia la clase SqliteDatabase perteneciente a peewee con el nombre de la base de datos:

.. code-block:: python

   db = SqliteDatabase('lavadero.db')


Clases
-------

En principio, genera una clase llamada BaseModel, que hereda de Model, y que se encarga de generar desde una clase de peewee, las condiciones para la creacion de la tabla.

.. code-block:: python

   class BaseModel(Model):
      class Meta:
         database = db

**Clase Ordenes:**

Clase que se encarga de generar e nombre, atributos y campos de la tabla a crear de la base de datos.

.. code-block:: python

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


**Clase OperacionesDB:**

Genera un constructor con la conexion y creación de la base de datos con sus tablas.

Esto logra que al instanciar la clase, la misma generara la conexion con la base de datos y las tablas, el cual seran utilizadas en otras clases.

.. code-block:: python

   class OperacionesDB:
      def __init__(self):
         try:
            db.create_tables([Ordenes])
            print("Conexion con base de datos OK\nTablas creadas OK")
         except DatabaseError as dbe:
            print("Error en la base de datos:", dbe)
         except Exception as err:
            print("Ocurrio un error inesperado:", err)


**Clase OperacionesCRUD:**

Representa las operaciones de la base de datos:
- Alta
- Baja
- Modificacion
- Consulta
- Exportacion
- Borrado total


**Metodos de clase:**

**Alta:**

Metodo que permite generar una nueva orden.

Parametros:

- **nombre:** Nombre de la persona que realiza la orden.
- **telefono:** Telefono de la persona que realiza la orden.
- **tipo:** Tipo de la orden (completo, secado, etc.)
- **cantidad:** Cantidad de la orden.
- **fecha:** Fecha de entrega de la orden.
- **horario:** Horario de entrega de la orden (Mañana, Mediodia o Tarde).
- **precio:** Precio de la orden.

.. code-block:: python

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
            print("***" * 10)
            print("Nueva orden generada:",nueva_orden)
            print(f"Nombre: {nombre}\nTelefono: {telefono}\nTipo: {tipo}\nCantidad: {cantidad}\nFecha de entrega: {fecha}\nHorario: {horario}\nPrecio: $ {precio}\n")
            print("***" * 10)
      except DataError as de:
         print("Error con los datos:", de)
      except IntegrityError as ie:
         print("Error de integridad:", ie)
      except Exception as err:
         print("Ocurrio un error inesperado:", err)


**Baja:**

Metodo que permite borrar una orden existente.

Obtiene como parametro el id de la orden, y la borra en la base de datos.

.. code-block:: python

   def borrar_orden(self, id):
      try:
         if not id and not isinstance(id, int):
            print(f"Error, el ID {id} es invalido.")
         else:
            self.id = id
            borrar = Ordenes.get(id)
            borrar.delete_instance()
            print("***" * 10)
            print(f"Se ha borrado la orden {id}")
            print("***" * 10)
      except DoesNotExist as ne:
         print("El ID {id} no existe:", ne)
      except Exception as err:
         print("Ocurrio un error inesperado:", err)


**Modificar:**

Metodo que permite modificar una orden existente.

Obtiene como parametro el id de la orden, y modifica la orden en la base de datos.
Al igual que en la orden, obtiene los siguientes parametros, ademas del id de la orden:

- **id:** Identificador de la orden que se selecciona.
- **nombre:** Nombre de la persona que realiza la orden.
- **telefono:** Telefono de la persona que realiza la orden.
- **tipo:** Tipo de la orden (completo, secado, etc.)
- **cantidad:** Cantidad de la orden.
- **fecha:** Fecha de entrega de la orden.
- **horario:** Horario de entrega de la orden (Mañana, Mediodia o Tarde).

.. code-block:: python

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
            print("***" * 10)
            print(f"Se ha modificado exitosamente la orden {id}.")
            print("***" * 10)
      except Exception as err:
            print("Ocurrio un error inesperado:", err)


**Consultar ordenes:**

Metodo que perimte consultar todas las ordenes vigentes en la base de datos.

Retorna:

- resultado: dict
   Diccionario con los datos de todas las ordenes.

.. code-block:: python

   def consulta_ordenes(self):
      try:
         resultado = Ordenes.select().dicts()
         return resultado
      except Exception as err:
         print("Ocurrio un error inesperado:", err)


**Consultar nombre:**

Metodo que permite realizar una consulta por nombre.

Obtiene como parametro el nombre de la persona a buscar, y retorna:

- resultado: dict
   Diccionario con los datos de las ordenes de la persona.

.. code-block:: python

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


**Borrar todas las ordenes:**

Metodo que permite borrar todas las ordenes existentes.

.. code-block:: python

   def borrar_todo(self):
      try:
         Ordenes.delete().execute()
         print("Todos los registros fueron borrados de la base de datos.")
      except Exception as err:
         print("Ocurrio un error inesperado", err)


**Exportar:**

Exporta todas las ordenes en un archivo .txt, en la raiz del proyecto con la fecha y hora de la exportacion.

.. code-block:: python

   def exportar_ordenes(self):
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