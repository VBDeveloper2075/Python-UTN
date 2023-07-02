import pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client["test_database"]        # equivalente a bases 
collection = db['test-collection']  # equivalente a tablas

# Ver bases
print(client.list_database_names())

# Ver colecciones
print(db.list_collection_names())  #Ver colecciones de mi base

mis_colecciones = db.list_collection_names()
if "test-collection" in mis_colecciones:
  print("Existe.")