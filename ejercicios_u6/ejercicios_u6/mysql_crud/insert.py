import mysql.connector

mibase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mi_plantilla2",
)

micursor = mibase.cursor()

sql="INSERT INTO producto (titulo) VALUES (%s)"
datos=("Producto 4",)
micursor.execute(sql, datos)
mibase.commit()