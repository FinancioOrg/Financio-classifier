import pymongo
import os

def fetch_categories():
    client = pymongo.MongoClient("mongodb+srv://btymofieienko:7MY7SZYz95T0cEXI@cluster0.xkyzxde.mongodb.net/?retryWrites=true&w=majority")
    # Database Name
    db = client["FinancioDB"]
    # Collection Name
    col = db["Collections"]
    cursor  = col.find({},{'_id':0,'Name':1})
    names = [document['Name'] for document in cursor]
    return names