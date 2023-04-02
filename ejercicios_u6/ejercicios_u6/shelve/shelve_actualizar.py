import shelve

db = shelve.open('persona')
juan = db['juan']
juan = {"nombre": "Juan Perez", "edad": 63}
db['juan']=juan
db.close()