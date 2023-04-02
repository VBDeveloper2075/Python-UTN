from tkinter import *

# por ahora hacemos la importacion con un asterisco (aunque no es muy conveniente)
master = Tk()
# en vez de master se puede poner el nombre que uno quiera, main, window, ventana. No hay más de una tk por apicación. Se maqueta de una sola forma (con grid o con pack), no mezclar.
el_id = Label(master, text="id")
# Con esto defino el elemento. Va por separado del posicionamiento que hago en el renglón de abajo. El id guarda el número que representa cada fila. Vamos a usar valores autoincrementales. Definimos un label y colocamos un texto de descripción. El label es un widget
el_id.grid(row=0, column=0, sticky=W)
# con esto ubico el label en una posición
nombre = Label(master, text="Nombre")
nombre.grid(row=1, column=0, sticky=W)
# el atributo sticky puedo mover el elemento como la rosa de los vientos, o sea este-oeste - norte-sur. W sería al oeste
entry_id = Entry(master)
# entry_id lo pongo dentro de master, es una entrada de datos
entry_id.grid(row=0, column=1)
entry_nombre = Entry(master)
entry_nombre.grid(row=1, column=1)


# funcion para que cada vez que alguien presione el botón se imprima la palabra hola
def funcion():
    print("Hola")


boton_g = Button(master, text="Guardar", command=funcion)
boton_g.grid(row=2, column=1)

master.mainloop()
