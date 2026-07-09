from dotenv import load_dotenv
import sys
import logging
import pandas as pd
from src.extract.extract_api_earthquakes import extract_earthquakes


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

df = extract_earthquakes()


def earthquake_transform() -> pd.DataFrame:
        
        records = []

        df["coordinates"] = df.drop(columns=["coordinates"], inplace=True)
        df["longitude"] = df["longitude"].astype(float)
        df["latitude"] = df["latitude"].astype(float)
        df["depth"] = df["depth"].astype(float)
        df["time"] = pd.to_datetime(df["time"], unit="ms")

        return pd.DataFrame(records)
