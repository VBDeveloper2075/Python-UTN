import sqlite3


def crear_base():
    con = sqlite3.connect("mibase.db")
    return con


def borrar(con, mi_id):
    cursor = con.cursor()
    mi_id = int(mi_id)
    data = (mi_id,)
    sql = "DELETE from personas where id = ?;"
    cursor.execute(sql, data)
    con.commit()


con = crear_base()
borrar(con, 6)

