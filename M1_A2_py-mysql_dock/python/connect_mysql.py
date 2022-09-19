import os
import pandas as pd
import pymysql
from sqlalchemy import create_engine

path = os.getcwd()

# Connect database
cnx = create_engine('mysql+pymysql://root:root@mysql/db')    

# Read the entire table
df = pd.read_sql('SELECT * FROM emp', cnx)

print(df)
# Save file to .CSV format
# os.chown(path=path+ "/data/", uid=2000)
# os.chmod(path+ "/data/employee_data.csv", 755)
df.to_csv(path+ "/data/employee_data.csv", index=False)
