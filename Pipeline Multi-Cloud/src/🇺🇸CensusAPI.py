import requests
import pandas as pd

def extract_census():
    url = "https://api.census.gov/data/2023/pep/population?get=NAME,POP&for=state:*"
    r = requests.get(url)
    data = r.json()

    df = pd.DataFrame(data[1:], columns=data[0])
    df["POP"] = df["POP"].astype(int)
    df["country"] = "USA"

    return df