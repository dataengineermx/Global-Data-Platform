import requests
import pandas as pd
from datetime import datetime




url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"
params={
        "minmagnitude": 3,  #Magnitud minima
        "starttime": "2026-01-01",
        "latitude": 19.4326,  #latitud y longitud aproximada correspondiente a Mexico
        "longitude": -99.1332,
        "maxradiuskm": 500
        }



r = requests.get(url, params=params)
data = r.json()


records = []

for e in data["features"]:
    records.append({
        "type": "earthquake",
        "magnitude": e["properties"]["mag"],
        "place": e["properties"]["place"],
        "time": datetime.fromtimestamp(e["properties"]["time"]/1000)
 #       "time_ori": e["properties"]["time"]
    })

df=pd.DataFrame(records)
print(df)
