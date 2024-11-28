Estilos
==============

Modulo que contiene los estilos de la interfaz de usuario.

El mismo permite, de forma sencilla, realizar cambios en los colores y fuentes de la interfaz de usuario.

**Importaciones requeridas:**

.. code-block:: python
   
   #Bibliotecas de terceros
   from tkinter import *


**Colores de fuente:**

.. code-block:: python
   
   COLOR_ERROR = "red"
   COLOR_OK = "green"
   COLOR_INFO = "black"
   COLOR_TITUTLO = "white"
   COLOR_SUBTITULO = "black"


**Estilos de fuente:**

.. code-block:: python
   
   TEXT_INFO = ("Arial", 13, "bold")
   TEXT_TITULO = ("Arial", 11, "bold")
   TEXT_HEADER = ("Arial", 9, "bold")
   TEXT_BUTTON = ("Arial", 9, "bold")


**Color de fondo (tema):**

.. code-block:: python
   
   MODO_OSCURO = "#353635"
   MODO_CLARO = "#ededed"
   MODO_VERDE = "#1cba46"


De esta forma, se puede realizar modificaciones en los colores de la inferfaz, sin manipular directamente los colores
de los demas modulos.