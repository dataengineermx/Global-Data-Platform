from datetime import datetime
import pandas as pd
import requests

url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"

params = {
    "minmagnitude": 3,              # Magnitud mínima
    "starttime": "2017-01-01",      #Fecha Inicio
    "latitude": 19.4326,            # LAT y LON de la CDMX, México
    "longitude": -99.1332,
    "maxradiuskm": 700,             #Radio de 500km
}

records = []

#Abre una sesión de internet que mantiene la conexión abierta eficientemente mientras dure este bloque de código
with requests.Session() as session:
 
    try:
#ntenta ejecutar las siguientes líneas, pero si algo falla, no te rompas; salta a la sección de errores

        response = session.get(url, params=params, timeout=(3.05, 27))

#Lanza una excepción si el servidor responde con error (4xx o 5xx)
#Verifica la respuesta del servidor. Si la página web da un error (como el famoso error 404 o 500), interrumpe el proceso para evitar trabajar con datos rotos.
        response.raise_for_status()

#Se define la variable 'data' convirtiendo la respuesta a JSON, Traduce la respuesta de texto que envió el servidor y la convierte en un diccionario de Python fácil de leer
        data = response.json()

# Procesa los datos dentro del bloque try para asegurarnos de que existen
        for e in data.get("features", []):
            records.append(
                {
                    "type": e["properties"]["type"],
                    "status": e["properties"]["status"],
                    "magnitude": e["properties"]["mag"],
                    "place": e["properties"]["place"],
                    "coordinates": e["geometry"]["coordinates"], 
                    "time": e["properties"]["time"]
 #                   "time": datetime.fromtimestamp(e["properties"]["time"] // 1000),  # Usamos una división entera (//) para evitar problemas de flotantes en timestamps
                }
            )
#Si en la sección del try se cayó el internet, falló la URL o el servidor estuvo caído, este bloque atrapa el problema, te avisa en la pantalla con un mensaje y evita que el programa se cierre con un error crítico.
    except requests.exceptions.RequestException as error:
        print(f"API Error occurred: {error}")

# Solo creamos el DataFrame si logramos recuperar registros
#if records Comprueba si la lista tiene datos



if records:
    df = pd.DataFrame(records)
    print("API get earthquake records properly")
else:
    print("There is no earthquakes records or there was aan error ot obtain API ouput.")
