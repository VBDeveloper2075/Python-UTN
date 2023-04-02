import re

patron1 = re.compile(r"((?P<name>ap8)(?(name)9|))")

mail = "ap89 ap8 rp8 rp4 w"
print(patron1.search(mail))
