import os

from bson.objectid import ObjectId
from pymongo import MongoClient


class Config(object):
    MONGO_URL = "mongodb://neighborlyappcosmosdb:y6jZlhf598jARnwExudgXXVb6fy5lReqSEoopUtndDByhfHbe5R9MvJ2qgERaAYKci7DjNT2E64dPf7sYw5PEQ==@neighborlyappcosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@neighborlyappcosmosdb@"  # TODO: Update with appropriate MongoDB connection information
            
    MONGO_DB_NAME = os.environ["MangoDBName"]


class MongoUnitOfWork:
    def __init__(self, config=Config):
        self.client = MongoClient(config.MONGO_URL)
        self.db = self.client[config.MONGO_DB_NAME]

    def get_all(self, collection_name):
        collection = self.db[collection_name]
        result = collection.find({})
        return result

    def get_one(self, collection_name, id):
        collection = self.db[collection_name]
        query = {"_id": ObjectId(id)}
        print(query)
        #query = {"_id": id}
        result = collection.find_one(query)
        return result

    def delete_by_id(self, collection_name, id):
        collection = self.db[collection_name]
        query = {"_id": ObjectId(id)}
        #query = {"_id": id}
        result = collection.delete_one(query)
        return result

    def update_by_id(self, collection_name, id, request):
        collection = self.db[collection_name]
        filter_query = {"_id": ObjectId(id)}
        #filter_query = {"_id": id}
        update_query = {"$set": eval(request)}
        rec_id1 = collection.update_one(filter_query, update_query)
        return rec_id1

    def insert_one(self, collection_name, request):
        collection = self.db[collection_name]
        rec_id1 = collection.insert_one(eval(request))
        return rec_id1
