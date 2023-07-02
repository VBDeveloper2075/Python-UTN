print(ord("a"))
print(chr(97))
print(hex(97))

mi_string="hola"
print(mi_string.encode("ascii"))
print(mi_string.encode("utf32"))

var=b'\xff\xfe\x00\x00h\x00\x00\x00o\x00\x00\x00l\x00\x00\x00a\x00\x00\x00'
print(var.decode("utf32"))


