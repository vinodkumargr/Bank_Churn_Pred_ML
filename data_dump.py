import pymongo
import pandas as pd
import json, os
from dotenv import load_dotenv

load_dotenv()
mongodb_url = os.getenv("MONGO_DB_URL")

client = pymongo.MongoClient(mongodb_url)


DATA_FILE_PATH = "/home/vinod/projects_1/bank_churn_pred/churn.csv"
DATABASE_NAME = "BANK_CHURN"
COLLECTION_NAME = "BANK_CHURN"


if __name__ == "__main__":
    data = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns : {data.shape}")
        
    json_record = list(json.loads(data.T.to_json()).values())
    print(json_record[0])
    
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)