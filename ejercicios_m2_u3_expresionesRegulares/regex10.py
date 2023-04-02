import re

patron1 = re.compile(
    r"""\d +  # Parte entera
                   \.    # Punto decimal
                   \d *  # Parte de fracción""",
    re.X,
)

mail = "3.3"
print(patron1.search(mail))
