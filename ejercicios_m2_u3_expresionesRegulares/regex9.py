import re

patron1 = re.compile(r"(<)?(\w+@\w+(?:\.[a-z]+)+)(?(1)>|$)", re.I)

mail = "<user@host.Com>"
print(patron1.search(mail))

patron2 = re.compile(r"(<)?(\w+@\w+(?i:\.[a-z]+)+)(?(1)>|$)")
mail1 = "<user@host.Com>"
print(patron2.search(mail1))
