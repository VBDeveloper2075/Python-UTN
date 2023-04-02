import sqlite3

def crear_base():
    con = sqlite3.connect('mibase.db')
    return con

def crear_tabla(con):

    cursor = con.cursor()
    sql = "CREATE TABLE personas(id integer PRIMARY KEY, nombre text)"
    cursor.execute(sql)
    con.commit()

con = crear_base()
crear_tabla(con)
