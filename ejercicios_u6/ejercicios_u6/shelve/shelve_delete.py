import shelve

db = shelve.open('persona')
del db['juan'] 
db.close()