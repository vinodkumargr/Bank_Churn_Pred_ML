from src.logger import logging
from src.exception import ChurnException
from src import config
import pandas as pd
import numpy as np
import os, sys
import yaml, pickle


def get_df(database_name:str, collection_name:str) -> pd.DataFrame:
    try:

        df = pd.DataFrame(list(config.mongo_client[database_name][collection_name].find()))


        if "__id" in df.columns:
            df = df.drop(columns=['__id'], axis=1)

        return df

    except Exception as e:
        raise ChurnException(e, sys)
    

def save_numpy_array_data(file_path: str, array: np.array):

    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise ChurnException(e, sys)
    

def load_numpy_array_data(file_path: str):
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise ChurnException(e, sys)
    


def save_object(file_path: str, obj: object) -> None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise ChurnException(e, sys)
    

def load_object(file_path:str)->object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"file path : {file_path} not exists...")
        with open(file_path , "rb") as file_obj:
            return pickle.load(file_obj)
        
    except Exception as e:
        raise ChurnException(e, sys)
    