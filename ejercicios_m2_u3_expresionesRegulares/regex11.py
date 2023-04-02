import re

patron1 = re.search(
    r"un.", "Hola esto es una prueba, se escribe de nuevo un hola", flags=0
)

print(patron1)
