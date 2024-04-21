from pymongo import MongoClient


class MongoDBClient:
    def __init__(self):
        uri = "mongodb+srv://vicherver:xwUiKssJ7ro9xNHW@cluster0.ungjrns.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client = MongoClient(uri)
        self.db = self.client['score']
        self.collection = self.db["score"]

    def close_connection(self):
        self.client.close()

