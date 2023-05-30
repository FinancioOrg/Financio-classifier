import pymongo
import os

def fetch_categories():
    connstr = os.environ.get('MONGO')
    client = pymongo.MongoClient(connstr)
    # Database Name
    db = client["FinancioDB"]
    # Collection Name
    col = db["Collections"]
    cursor  = col.find({},{'_id':0,'Name':1})
    names = [document['Name'] for document in cursor]
    return names