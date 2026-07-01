import pandas as pd
import logging
from paths import data_raw_path
from extract_api_population import df



try:
    
    df.to_csv(data_raw_path/"population.csv", index=False)
    logging.info("File loaded successfully")

except Exception as e:
    print(type(e).__name__, e)
    logging.error("Error when loading records")