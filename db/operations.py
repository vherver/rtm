from bson import ObjectId
from db.client import MongoDBClient


class MongoDBOperations:
    def __init__(self):
        self.client = MongoDBClient()

    def get_scores(self):
        return self.client.collection.find()

    def find_score_by_id(self, score_id):
        return self.client.collection.find_one({"_id": ObjectId(score_id)})

    def insert_score(self, score_data):
        self.client.collection.insert_one(score_data)
        self.client.close_connection()
