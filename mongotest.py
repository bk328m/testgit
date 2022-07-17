import pymongo
client = pymongo.MongoClient("mongodb+srv://bk328m:Dad2022@bhavesh.8n4kg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={
    "name":"sudhanshu",
    "email":"ssdsdsdssdfsf",
    "surname":"kumar"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
