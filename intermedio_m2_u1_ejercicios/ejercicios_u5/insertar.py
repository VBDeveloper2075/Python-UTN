import pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client["test_database"]
collection = db['test-collection']

mi_diccionario = {
    "nombre": "Ana", 
    "edad": 33, 
    "estado_civil": True,
    "esposo": "Pablo",
    "hijos": ["Cecilia","Luis"],
    "dni":778856789
}

registro = collection.insert_one(mi_diccionario)
print(registro.inserted_id)
