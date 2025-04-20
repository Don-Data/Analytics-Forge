# utils/load_env.py
from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()
    return {
        "SNOWFLAKE_USER": os.getenv("SNOWFLAKE_USER"),
        "SNOWFLAKE_PASSWORD": os.getenv("SNOWFLAKE_PASSWORD"),
        "DBT_TARGET": os.getenv("DBT_TARGET"),
        # add more as needed
    }