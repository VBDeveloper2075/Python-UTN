mi_string="Hola soy Juan"
mi_bytearray=bytearray(mi_string, "latin1")
print(mi_bytearray)
print(mi_bytearray[5])
mi_bytearray[5]=117
print(mi_bytearray)
print(mi_bytearray.decode("latin1"))