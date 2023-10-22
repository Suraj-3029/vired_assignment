from pymongo.mongo_client import MongoClient
from bson import json_util
import json

client = None


def connect_mongo(host, username, password):
    uri = f"mongodb+srv://{username}:{password}@{host}/Configurations?retryWrites=true&w=majority"
    try:
        # Create a new client and connect to the server
        client = MongoClient(uri)
        return client
    except Exception as e:
        print("error while connecting", e)


def save(client, data):
    db_name = "suraj"
    collection_name = "config"
    try:
        if not client:
            return
        db = client[db_name]
        coll = db[collection_name]
        data_sanitized = json.loads(json_util.dumps(data))
        coll.insert_one(data_sanitized)
    except Exception as e:
        print("error while insert", e)
