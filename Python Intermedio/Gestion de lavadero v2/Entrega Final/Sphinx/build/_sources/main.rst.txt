Main
===========

Introducción
------------
Es el modulo que se ejecuta para el inicio de la aplicación.

Este módulo utiliza las siguientes importaciones:

.. code-block:: python

   from controlador import *

La importación, permitira acceder a las clases y funciones de la clase Controlador y OperacionesDB.
Por lo cual, una ves que se ejecute el siguiente codigo, la aplicación se ejecutara:

Ejecución de la app
-------------------
.. code-block:: python

   if __name__ == "__main__":
      app = Controller()
      db = OperacionesDB()
      app.ventana.mainloop()

La clase Controller se encarga de la creación de la interfaz de usuario, mientras que la clase OperacionesDB se encarga de la conexión con la base de datos.

Al iniciar, mostrara la ventana principal de la aplicación, y mostrará todas las ordenes vigentes en la base de datos.

.. image:: ../img/ventana_principal.jpg
   :alt: Ventana principal
   :width: 600px
   :align: center

De esta forma, la aplicacion estara lista para ser utilizada.