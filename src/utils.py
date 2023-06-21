from src.logger import logging
from src.exception import ChurnException
from src import config
import pandas as pd
import os, sys


def get_df(database_name:str, collection_name:str) -> pd.DataFrame:
    try:

        df = pd.DataFrame(list(config.mongo_client[database_name][collection_name].find()))


        if "__id" in df.columns:
            df = df.drop(columns=['__id'], axis=1)

        return df

    except Exception as e:
        raise ChurnException(e, sys)