import shelve

db = shelve.open('persona')
for key in db:
    print(key, '==> ', db[key]['nombre'], db[key]['edad'])
db.close()