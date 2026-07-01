import pandas as pd
import logging
from paths import data_raw_path
from extract_api_population import df


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

logging.info("Inicio de carga")
#logging.info("Archivo leído correctamente")
#logging.error("Error al insertar registros")

df.to_csv(data_raw_path/"population.csv", index=False)