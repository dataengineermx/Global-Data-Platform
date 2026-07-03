from dotenv import load_dotenv
import os
import psycopg

load_dotenv()   # <-- this loads the .env file


print("HOST:", os.getenv("DB_HOST"))
print("PORT:", os.getenv("DB_PORT"))
print("DB:", os.getenv("DB_NAME"))
print("USER:", os.getenv("DB_USER"))

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


cur.execute("CREATE TABLE IF NOT EXISTS earthquakes(
    types STRING,
    status STRING,
    magnitude DOUBLE,
    place STRING,
    longitud DOUBLE,
    latitud DOUBLE,
    altitud DOUBLE
    time TIMESTAMP
    );")
resultado = cur.fetchone()
print(resultado)


#Close cur
cur.close()
conn.close()
