import pprint

from pymongo import MongoClient
import json


with open("./credentials.json") as f:
    json_content = f.read()
    
cred = json.loads(json_content)



connection = f'mongodb+srv://{cred["username"]}:{cred["password"]}@cluster0.mb0zwid.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(connection)


db = client.sample_restaurants

collection = db.restaurants


for doc in collection.find({'name': 'La Bella Pizza'}):
    pprint.pprint(doc)

