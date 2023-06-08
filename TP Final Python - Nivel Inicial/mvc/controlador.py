from modelo import conexion, crear_tabla
from vista import tree
from tkinter.messagebox import showinfo

# from PIL import ImageTk, Image
import re
import os

con = conexion()
crear_tabla(con)

# --------------------------FUNCIONES--------------------------#


def mostrar(con):
    cursor = con.cursor()
    sql = "SELECT * FROM pacientes"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado:
        tree.insert(  # inserto cada elemento de la tupla
            "",
            "end",
            text=i[0],
            values=(i[1], i[2], i[3], i[4], i[5]),
        )


try:
    conexion()
    crear_tabla()
except:
    print("Ya existe la tabla, puede editar")


# Agregar
def funcion_a(paciente, especialidad, dia, hora, obra_social, tree):
    cadena = paciente
    patron = "^[A-Za-z]+(?i:[_-]+)*$"
    if re.match(patron, cadena):
        con = conexion()
        cursor = con.cursor()
        data = (paciente, especialidad, dia, hora, obra_social)
        sql = "INSERT INTO pacientes (paciente, especialidad, dia, hora, obra_social) VALUES (?,?,?,?,?)"
        cursor.execute(sql, data)
        con.commit()
        showinfo("Agregar", "Turno añadido")
        actualizar_treeview(tree)
    else:
        print("error en carga")


# Editar
def funcion_b(paciente, especialidad, dia, hora, obra_social, tree):
    cadena = paciente
    patron = "^[A-Za-záéíóú]*$"
    if re.match(patron, cadena):
        valor = tree.selection()
        item = tree.item(valor)
        cursor = con.cursor()
        data = (
            entry_paciente.get(),
            entry_especialidad.get(),
            entry_dia.get(),
            entry_hora.get(),
            entry_obra_social.get(),
            str(item["text"]),
        )
        sql = "UPDATE pacientes SET paciente = ?, especialidad = ?, dia = ?, hora = ?, obra_social = ? WHERE id = ?"
        cursor.execute(sql, data)
        con.commit()
        showinfo("Editar", "Turno Modificado")
        actualizar_treeview(tree)  # actualizas el tree
    else:
        print("error en carga")


# Borrar
def funcion_c(tree):
    valor = tree.selection()
    item = tree.item(valor)
    mi_id = item["text"]
    showinfo("Borrar", "Registro borrado")
    con = conexion()
    cursor = con.cursor()
    data = (mi_id,)
    sql = "DELETE FROM pacientes WHERE id = ?;"
    cursor.execute(sql, data)
    con.commit()
    tree.delete(valor)


# Actualizar
def actualizar_treeview(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)
    sql = "SELECT * FROM pacientes ORDER BY id ASC"
    con = conexion()
    cursor = con.cursor()
    datos = cursor.execute(sql)
    resultado = datos.fetchall()
    for fila in resultado:
        mitreview.insert(
            "", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5])
        )


mostrar(con)
