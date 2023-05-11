import os
import snowflake.connector
from snowflake.connector import *
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas

account = os.environ['SF_ACCOUNT']
password = os.environ['SF_PASSWORD']
username= os.environ['SF_USERNAME']


print(f"SF ACCOUNT IS:  {account}")
print(f"SF PASSWORD IS:  {password}")
print(f"SF USERNAME IS:  {username}")

print("Vamos testar a connecção")

connection = snowflake.connector.connect (
    user=username,
    password=password,
    account=account

)

print("Conectou")
