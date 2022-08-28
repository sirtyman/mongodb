import pprint
from pymongo import MongoClient


connection = "mongodb+srv://sirtyman:<passwd>@cluster0.mb0zwid.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection)

db = client.sample_restaurants
collection = db.restaurants

for doc in collection.find({'name': 'La Bella Pizza'}).batch_size(1000):
    pprint.pprint(doc)
