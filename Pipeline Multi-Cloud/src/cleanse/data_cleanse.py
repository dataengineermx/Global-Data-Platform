from dotenv import load_dotenv
import os
import psycopg

load_dotenv()   # <-- this loads the .env file

print("DB_HOST")


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
