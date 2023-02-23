import sqlite3


def crear_base():
    con = sqlite3.connect('mibase.db')
    return con

def actualizar(con, mi_id, nombre):
    cursor = con.cursor()
    mi_id = int(mi_id)
    data = (nombre, mi_id)
    sql = "UPDATE personas SET nombre=? WHERE id=?;"
    cursor.execute(sql, data)
    con.commit()

con = crear_base()

actualizar(con, 3, "Anna22")

