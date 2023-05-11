import snowflake.connector
import os
from snowflake.connector import *
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas

print('estou a ler')

conn = snowflake.connector.connect(
    user=os.environ.get('SF_USERNAME'),
    password=os.environ.get('SF_PASSWORD'),
    # account = 'px51283.eu-west-3.aws'
    account=os.environ.get('SF_ACCOUNT')
    # database = 'DEV'
    #,
#    schema = 'RAW'    
    )

cursor = conn.cursor()
cursor.execute("SELECT * FROM DEV.RAW.TITANIC_TRAIN_RAW;")
print("connection is donne")