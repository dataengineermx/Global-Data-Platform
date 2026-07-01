import pandas as pd
from paths import data_raw_path
from extract_api_population import df
from job_monitor import LoadMonitor
from logger_config import get_logger

logger = get_logger("load_population")

start_time = time.time()



job_monitor = LoadMonitor("LOAD_CSV_POPULATION")
job_monitor.start()
records = len(df)




try:
    df.to_csv(data_raw_path/"population.csv", index=False)
    job_monitor.success(records)

except Exception as e:
    print(type(e).__name__, e)
