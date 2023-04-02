import sqlite3


def crear_base():
    con = sqlite3.connect('mibase.db')
    return con

def insertar(con, mi_id, nombre):
    cursor = con.cursor()
    mi_id = int(mi_id)
    data = (mi_id, nombre)
    sql = "INSERT INTO personas(id, nombre) VALUES(?, ?)"
    cursor.execute(sql, data)
    con.commit()

con = crear_base()

insertar(con, 3, "Anna2")
insertar(con, 4, "Anna2")
insertar(con, 5, "Anna2")
insertar(con, 6, "Anna2")

