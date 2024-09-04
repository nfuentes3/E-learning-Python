import sqlite3

def crear_base():
    con = sqlite3.connect("mibase.db")
    return con

def selecionar(con, mi_id):
    cursor = con.cursor()
    mi_id = int(mi_id)
    data = (mi_id, )
    sql = "SELECT * FROM personas WHERE id = ?"
    cursor.execute(sql, data)
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)

con = crear_base()
selecionar(con, 3)