import pandas as pd
import logging
from paths import data_raw_path
from extract_api_population import df

#Execution Controls
logging.basicConfig(
level=logging.INFO,
format='%(asctime)s | %(levelname)s | %(message)s')

total_leidos = 0
total_insertados = 0
total_rechazados = 0


logging.info("Load started"),
logging.info(
    f"Leídos={total_leidos}, "
    f"Insertados={total_insertados}, "
    f"Rechazados={total_rechazados}"             
             )

try:
    
    df.to_csv(data_raw_path/"population.csv", index=False)
    logging.info("File loaded successfully")

except Exception as e:
    print(type(e).__name__, e)
    logging.error("Error when loading records")