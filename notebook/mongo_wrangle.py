import pandas as pd
from pymongo import MongoClient
def get_data(port,host,db,col):
    client=MongoClient(f"mongodb://{host}:{port}")
    database=client[db]
    collection=database[col]
    df =pd.DataFrame(list(collection.find({},{"_id":0})))
    client.close()
    return df



