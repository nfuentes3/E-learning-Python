import mysql.connector

mibase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

micursor = mibase.cursor()
micursor.execute("CREATE DATABASE mi_plantilla2")