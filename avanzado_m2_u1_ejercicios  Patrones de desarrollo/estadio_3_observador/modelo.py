import sqlite3
from peewee import *
import datetime
from observador import Sujeto

try:
    db = SqliteDatabase("nivel_avanzado.db")

    class BaseModel(Model):
        class Meta:
            database = db

    class Noticia(BaseModel):
        titulo = CharField(unique=True)
        descripcion = TextField()

        def __str__(
            self,
        ):
            return "El título es: " + self.titulo

    db.connect()
    db.create_tables([Noticia])

except:
    print("mmmm")


class Abmc(Sujeto):
    def __init__(
        self,
    ):
        print("en controlador")

    def actualizar_treeview(self, mitreeview):
        # limpieza de tabla
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)

        for valor_recuperado in Noticia.select():
            mitreeview.insert(
                "",
                0,
                text=valor_recuperado.id,
                values=(
                    valor_recuperado.titulo,
                    valor_recuperado.descripcion,
                    valor_recuperado,
                ),
            )

    def alta(self, titulo, descripcion, mitreeview):

        noticia = Noticia()
        noticia.titulo = titulo.get()
        noticia.descripcion = descripcion.get()
        noticia.save()
        self.titulo = titulo.get()
        self.descripcion = descripcion.get()
        self.actualizar_treeview(mitreeview)
        # ****************************************************
        # Puedo llamar a notificar
        # ****************************************************
        self.notificar(titulo.get(), descripcion.get())

    def baja(self, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        borrar = Noticia.get(Noticia.id == valor_id["text"])
        borrar.delete_instance()
        self.actualizar_treeview(mitreeview)

    def modificar(self, titulo, descripcion, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        actualizar = Noticia.update(
            titulo=titulo.get(), descripcion=descripcion.get()
        ).where(Noticia.id == valor_id["text"])
        actualizar.execute()

        self.actualizar_treeview(mitreeview)
