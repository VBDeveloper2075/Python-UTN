import pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client["test_database"]
collection = db['test-collection']

#para eliminar uno delete_one()
# solo elimina el primero que encuentra si existe
documento = collection.delete_one({
    "dni":443456789
})
#Puedo borrar muchos por regex
borrar_m = { "nombre": {"$regex": "^A"} }

x = collection.delete_many(borrar_m)

# para eliminar muchos delete_many()