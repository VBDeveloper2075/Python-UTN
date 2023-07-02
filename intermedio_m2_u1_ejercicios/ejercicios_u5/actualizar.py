import pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client["test_database"]
collection = db['test-collection']

#para actualizar uno update_one()
 
collection.update_one({
    "edad":14
},{
    "$set":{
        "edad":15
    }
}
)
#para actualizar muchos update_many()
antes = { "nombre": { "$regex": "^P" } }
despues = { "$set": { "nombre": "Pepe" } }

collection.update_many(antes, despues)