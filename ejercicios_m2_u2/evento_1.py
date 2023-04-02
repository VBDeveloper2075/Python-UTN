from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename

master = Tk()


def funcion():
    # ruta = askopenfilename()
    # print(ruta)
    resultado = askcolor(color="#00ff00", title="El título")
    print(resultado)
    print(resultado[1])


"""
0 1 2 3 4 5 6 7 8 9 a b c d e f
rojo     verde     azul
ff         00       00
00         00       00
ff         ff       ff 



#ac135b
"""
"""
C:/Users/usuario/Desktop/ejercicios_u5/img/mascotas.jpg
"""

boton_g = Button(master, text="Guardar", command=funcion)
boton_g.grid(row=2, column=1)

master.mainloop()
