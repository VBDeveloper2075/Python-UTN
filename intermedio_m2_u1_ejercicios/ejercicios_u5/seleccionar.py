import pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client["test_database"]
collection = db['test-collection']

# Recupero todos los documentos
print(collection.find({}))

for x in collection.find({}):
    print(x)
print("---"*21)
# Uso de filtros
# Recupero edad mayor a 20
for x in collection.find({
    'edad':{
        "$gt":20
    }
}):
    print(x)
print("---"*21)
# Recupero un solo elemento
documento = collection.find_one({
    "dni":443456789
})
print(documento)