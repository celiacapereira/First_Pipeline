import snowflake.connector
import os
from snowflake.connector import *
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
from dotenv import load_dotenv


print('estou a ler')

# conn = snowflake.connector.connect(
#     user=os.environ.get('SF_USERNAME'),
#     password=os.environ.get('SF_PASSWORD'),
#     # account = 'px51283.eu-west-3.aws'
#     account=os.environ.get('SF_ACCOUNT')
#     # database = 'DEV'
#     #,
# #    schema = 'RAW'    
#     )

    # Get the credentials from .env
SF_ACCOUNT    = os.getenv('SF_ACCOUNT')
SF_USER       = os.getenv('SF_USER')
SF_WAREHOUSE  = 'COMPUTE_WH'
SF_DATABASE   = 'DEV'
SF_SCHEMA     = 'RAW'
SF_PASSWORD   = os.getenv('SF_PASSWORD')

connection = snowflake.connector.connect (
account  = SF_ACCOUNT,
user     = SF_USER,
password = SF_PASSWORD,
warehouse = SF_WAREHOUSE,
database = SF_DATABASE,
schema   = SF_SCHEMA
)

# cursor = conn.cursor()
# cursor.execute("SELECT * FROM DEV.RAW.TITANIC_TRAIN_RAW;")
# print("connection is donne")