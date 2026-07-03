from src.utils.paths import data_raw_path
from src.extraction.extract_api_earthquakes import df
from src.monitor.job_monitor import LoadMonitor


def main():  #This prevents the code from executing accidentally when the module is imported by another module
    job_monitor = LoadMonitor("load_to_csv_earthquakes")
    job_monitor.start()

    try:

        records = len(df)
        df.to_csv(data_raw_path/"earthquakes.csv", index=False)
        job_monitor.success(records)

    except Exception as error:
        job_monitor.failed(error)

if __name__ == "__main__":
    main()