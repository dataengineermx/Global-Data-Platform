##  MX INEGI

import requests

url_inegi = "https://inegi.org.mx/servicios/api_indicadores.html" placeholder real requiere token

# simulación de respuesta estructurada
mexico = {
    "country": "Mexico",
    "year": 2023,
    "population": 129000000
}



##  US Census API
import requests

url_census = "https://api.census.gov/data/2023/pep/population?get=NAME,POP&for=state:*"

r = requests.get(url_census)
data = r.json()

# convertir a formato usable
usa = []

for row in data[1:]:
    usa.append({
        "country": "USA",
        "state": row[0],
        "population": int(row[1])
    })

print("Census: ", data)


##  Terremotos recientes


import requests

url_terre = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"

r = requests.get(url_terre)
data = r.json()

earthquakes = []

for eq in data["features"][:5]:
    earthquakes.append({
        "type": "earthquake",
        "magnitude": eq["properties"]["mag"],
        "place": eq["properties"]["place"]
    })

print("Earthquakes:", earthquakes)