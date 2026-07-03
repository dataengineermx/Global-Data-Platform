import pandas as pd
from paths import data_raw_path
from extract_api_earthquakes import df
from job_monitor import LoadMonitor

job_monitor = LoadMonitor("01_load_to_csv_earthquakes")
job_monitor.start()

try:

    records = len(df)
    df.to_csv(data_raw_path/"earthquakes.csv", index=False)
    job_monitor.success(records)

except Exception as error:
    job_monitor.failed(error)