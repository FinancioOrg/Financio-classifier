import pymongo

def fetch_categories():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Database Name
    db = client["FinancioDB"]
    # Collection Name
    col = db["Collections"]
    cursor  = col.find({},{'_id':0,'Name':1})
    names = [document['Name'] for document in cursor]
    return names