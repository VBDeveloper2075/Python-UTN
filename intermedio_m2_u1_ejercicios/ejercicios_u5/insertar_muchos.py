import pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client["test_database"]
collection = db['test-collection']

mi_diccionario = {
    "nombre": "Pedro", 
    "edad": 13, 
    "estado_civil": False,
    "dni":123456789
 
 
}
mi_diccionario2 = {
    "nombre": "José", 
    "edad": 40, 
    "estado_civil": True,
    "esposo": "Celeste",
    "hijos": ["Mora"], 
    "dni":443456789
}
registro = collection.insert_many([mi_diccionario, mi_diccionario2])
#print(registro.inserted_id)
