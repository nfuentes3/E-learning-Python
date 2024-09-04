import sqlite3

def crear_base():
    con = sqlite3.connect("mibase.db")
    return con

crear_base()