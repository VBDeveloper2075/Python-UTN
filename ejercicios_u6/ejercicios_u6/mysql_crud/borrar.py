import mysql.connector

mibase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mi_plantilla2",
)

micursor = mibase.cursor()

sql="DELETE FROM producto WHERE id =%s"
datos=("1",)
micursor.execute(sql, datos)
mibase.commit()