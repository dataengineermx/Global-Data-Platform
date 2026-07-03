#from datetime import datetime
from src.utils.paths import data_raw_path
from src.extraction.extract_api_population import df
from src.monitor.job_monitor import LoadMonitor



job_monitor = LoadMonitor("load_to_csv_population")
job_monitor.start()


try:
    records = len(df)
    df.to_csv(data_raw_path/"population.csv", index=False)
    
    job_monitor.success(records)

except Exception as error:
    job_monitor.failed(error)