import pandas as pd
import logging
from paths import data_raw_path
from extract_api_population import df
from logging_config import logging
from logging_config import config_my_logger
from logging_config import obtener_resumen

logger = config_my_logger("Job 01_load_population")
logger.info("Job Started")
try:
    
    df.to_csv(data_raw_path/"population.csv", index=False)
    logging.info("File loaded successfully")
    obtener_resumen("Resumen")

except Exception as e:
    print(type(e).__name__, e)
    logging.error("Error when loading records")