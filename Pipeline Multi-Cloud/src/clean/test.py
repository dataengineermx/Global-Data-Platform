from dotenv import load_dotenv
import os
import sys
import psycopg
import logging
import pandas as pd
from src.utils.cleanse import remove_parentesis
from src.utils.cleanse import milliseconds_to_date
from src.utils.paths import data_raw_path
from src.utils.paths import data_clean_path
from datetime import datetime


# Setup Structured Production Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("DB_LOADER")

### Loads the .env file
load_dotenv()    


##Data Transformations
df = pd.read_csv(data_raw_path/"earthquakes.csv")

df[["longitude", "latitude", "depth"]] = (
    df["coordinates"]
      .str.strip("[]")
      .str.split(", ", expand=True)
)

# Convert to numeric types
df["longitude"] = df["longitude"].astype(float)
df["latitude"] = df["latitude"].astype(float)
df["depth"] = df["depth"].astype(float)
df["time"] = pd.to_datetime(df["time"], unit="ms")
df["coordinates"] = df.drop(columns=["coordinates"], inplace=True)

df = df[
    [
        "type",
        "status",
        "magnitude",
        "place",
        "time",
        "longitude",
        "latitude",
        "depth"
    ]
]

#Store cleaned data
df.to_csv(data_clean_path/"clean_earthquakes.csv", index=False)

print(df.columns.tolist())