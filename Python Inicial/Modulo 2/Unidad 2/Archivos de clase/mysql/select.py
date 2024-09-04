import mysql.connector

mibase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mi_plantilla2",
    )

micursor = mibase.cursor()

sql = "SELECT * FROM producto"
micursor.execute(sql)

resultado = micursor.fetchall()
for x in resultado:
    print(x)
#datos = ("Producto2",)
#micursor.execute(sql, datos)
mibase.commit()