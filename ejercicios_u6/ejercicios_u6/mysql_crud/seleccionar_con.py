import mysql.connector

mibase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mi_plantilla2",
)

micursor = mibase.cursor()

titulo = "titulo"
sql="SELECT * FROM producto WHERE id = %s AND " + titulo + "= %s"
datos=(2, "Producto 2")
micursor.execute(sql, datos)

resultado = micursor.fetchall()

for x in resultado:
    print(x)