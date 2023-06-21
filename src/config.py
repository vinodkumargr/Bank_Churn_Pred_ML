import pymongo
import pandas as pd
import numpy as np
import json
import os, sys
from dotenv import load_dotenv
from dataclasses import dataclass

DATABASE_NAME = "BANK_CHURN"
COLLECTION_NAME = "BANK_CHURN"
load_dotenv()

mongo_client = pymongo.MongoClient(os.getenv("MONGO_DB_URL"))
#TARGET_COLUMN = "charges"
print(f"mongo client: {mongo_client}")