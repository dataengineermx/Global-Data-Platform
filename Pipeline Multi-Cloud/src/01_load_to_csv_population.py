import pandas as pd
import logging
from paths import data_raw_path
from extract_api_population import df

logging.basicConfig(
level=logging.INFO,
format='%(asctime)s | %(levelname)s | %(message)s')

logging.info("Load started")

try:
    
    with df.to_csv(data_raw_path/"population.csv", index=False) as f:

        logging.info("File loaded successfully")

except Exception as e:
    print(type(e).__name__, e)
    logging.error("Error when loading records")