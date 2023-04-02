import shelve

juan = {"nombre": "Juan Perez", "edad": 43}
susana = {"nombre": "Susana Gomez", "edad": 23}

db = shelve.open('persona')
db['juan'] = juan
db['susana'] = susana
db.close()