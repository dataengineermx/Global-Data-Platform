import requests
import pandas as pd


##Codes.alpha_2=MX for Mexico
##For Mexico        url = "https://api.restcountries.com/countries/v5?codes.alpha_2=MX"
##For North America url = "https://api.restcountries.com/countries/v5?region=Americas&subregion=North America"

url = "https://api.restcountries.com/countries/v5?region=Americas&subregion=North America&codes.alpha_2=MX"
headers = {
    "Authorization": "Bearer rc_live_4706e9734e7d4fccaa344055b59ef879"
}

response = requests.get(
    url,
    headers=headers,
    params={
## select only the values required from the API string
        "response_fields": "names.common,codes.alpha_2,population,region,subregion",  
        "limit": 10
    }
)

objects=response.json()["data"]["objects"]


data=[]

for country in objects:
    rows.append({
        "Region":country["region"],
        "SubRegion":country["subregion"],
        "Country_Name": country["names"]["common"],
        "Country_code": country["codes"]["alpha_2"],
        "Population": country["population"]
    })

#df = pd.DataFrame(rows)

if data:
    df = pd.DataFrame(data)
    print(df)
else:
    print("No se encontraron registros en poblacion o hubo un error en la solicitud.")