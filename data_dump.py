import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"
DATAFILE_PATH = "aps_failure_training_set1.csv"

if __name__ == "__main__":
    df = pd.read_csv(DATAFILE_PATH)
    print(f'Rows and Columns : ,{df.shape}')

    print('Converting to Json format')
    df.reset_index(drop = True,inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())

    print(f'Successfully converted to json here is value at first index {json_record[0]}')

    print('---------------------------------------Inserting to MongoDB ---------------------------------------------------')

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

    print('----------------------------------Successfully Inserted to MongoDB ---------------------------------------------------')