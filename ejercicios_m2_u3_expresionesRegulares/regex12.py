import re

retorno1 = re.split(r"\W+", "Palabras, palabras, palabras.")
retorno2 = re.split(r"(\W+)", "Palabras, palabras, palabras.")
retorno3 = re.split(r"\W+", "Palabras, palabras, palabras.", 1)
retorno4 = re.split("[a-f]+", "0a3B9", flags=re.IGNORECASE)

print(retorno1)
print(retorno2)
print(retorno3)
print(retorno4)
