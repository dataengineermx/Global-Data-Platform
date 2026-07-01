import pandas as pd

#Read earthquakes
from extract_api_earthquakes import df

df.to_csv("data/raw/earthquakes.csv", )