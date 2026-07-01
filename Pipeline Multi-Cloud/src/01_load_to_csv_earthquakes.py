import pandas as pd
from paths import data_raw_path

#Read earthquakes
from extract_api_earthquakes import df

df.to_csv(data_raw_path/"earthquakes.csv", index=False)