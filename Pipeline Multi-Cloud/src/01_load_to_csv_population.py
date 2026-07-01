import pandas as pd
from paths import data_raw_path

#Read earthquakes
from extract_api_population import data

data.to_csv(data_raw_path/"population.csv", index=False)