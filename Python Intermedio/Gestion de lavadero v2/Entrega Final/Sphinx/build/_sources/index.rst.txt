.. Gestor de ordenes para lavadero de ropa. documentation master file, created by
   sphinx-quickstart on Thu Nov 28 13:14:05 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Sistema de gestion de lavandería v1.0
============================================

Bienvenido a la documentacion del programa de gestor de ordenes para lavaderos de ropa, creado por Nicolas Fuentes.

.. warning:: Advertencia! El siguiente codigo se encuentra en desarrollo, por lo cual, no se recomienda utilizarlo en produccion.

Es un programa que permite gesionar, de forma digital, las ordenes de lavado de un negocio de lavanderia de ropa.
El objetivo es simplificar la gestion de las ordenes, obteniendo un control mas eficiente de las gestiones de servicios.

.. toctree::
   :maxdepth: 2
   :caption: Indice de modulos:

   main
   controlador
   modelo
   vista
   estilos


La aplicacion presenta una inferfaz sencilla, de una sola ventana, con el fin de faciilitar el uso a cualquier usuario que cuente con diferentes conocimientos y herramientas informáticas:

.. image:: ../img/ventana_principal.jpg
   :alt: Ventana principal
   :width: 600px
   :align: center


Funciones de la aplicacion:
---------------------------


La aplicacion cuenta con las siguientes funciones:

- **Alta:** Permite generar una nueva orden.
- **Baja:** Permite borrar una orden existente.
- **Modificar:** Permite modificar una orden existente.
- **Consultar:** Permite realizar una consulta por nombre.
- **Balance total:** Permite calcular el balance a cobrar total de las ordenes.
- **Exportar:** Permite exportar todas las ordenes.

Requerimientos:
---------------

Para poder ejecutar el programa, se debe tener instalado Python 3.x en el equipo.
Ademas, se deben instalar las siguientes librerias:

- Tkinter
- Peewee
- Tkcalendar

Para instalar las librerias, se debe ejecutar el siguiente comando en la terminal:

.. code-block:: python
   
   pip install -r requirements.txt

.. important:: Se recomienda instalar la app en un entorno virtual, para evitar conflictos con otras librerias instaladas en el equipo.

El archivo se encuentra en el .zip del proyecto.




