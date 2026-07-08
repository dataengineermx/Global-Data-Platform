from dotenv import load_dotenv
import os
import psycopg
import pandas as pd
from src.utils.cleanse import remove_parentesis
from src.utils.cleanse import milliseconds_to_date
from src.utils.paths import data_raw_path
from src.utils.paths import data_clean_path
from datetime import datetime


load_dotenv()   # <-- this loads the .env file

df = pd.read_csv(data_raw_path/"earthquakes.csv")

# transformations
t=1782943895600
test = milliseconds_to_date(t)

#atetime.fromtimestamp(e["properties"]["time"] // 1000)
#df["time"] = datetime.fromtimestamp(1782943895600)
#df["coordinates"] = remove_parentesis(df=df,columns=["coordinates"])["coordinates"]

print(test)

df.to_csv(data_clean_path/"clean_earthquakes.csv", index=False)

conn = psycopg.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)


cur = conn.cursor()

cur.execute("SELECT version();")
resultado = cur.fetchone()
print(resultado)


#Close cur
cur.close()
conn.close()
