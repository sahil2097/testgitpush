import pymongo

client = pymongo.MongoClient("mongodb+srv://sahil5723:NEWlife123@cluster0.1bbad.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name" : "sahil",
    "surname" : "arora",
    "email_id" : " sahil@gmail.com"
}

db1  = client['mongotest']
coll = db1['test']
coll.insert_one(d)