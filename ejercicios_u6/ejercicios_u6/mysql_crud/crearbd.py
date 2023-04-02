"""
pip install mysql-connector
pip install pymysql
pip install mysqlclient
pip install mysql-connector-python
"""
import mysql.connector  # importar la librería

mibase = mysql.connector.connect(
    host="localhost", user="root", password="", database="mis_libros"
)

micursor = mibase.cursor()
micursor.execute("CREATE DATABASE mi_plantilla2")
