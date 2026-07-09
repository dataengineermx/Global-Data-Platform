from airflow.sdk import dag, task
from datetime import datetime

from src.extract.extract_api_earthquakes import extract_earthquakes
from src.transform.earthquake_transform import earthquake_transform
from src.load.load_earthquakes import load_earthquakes


@dag(
    dag_id="earthquake_pipeline",
    schedule="@hourly",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["earthquakes", "etl"],
)
def earthquake_pipeline():

    @task
    def extract():
        return extract_earthquakes()

    @task
    def transform(df):
        return earthquake_transform(df)

    @task
    def load(df):
        load_earthquakes(df)

    raw_df = extract()
    transformed_df = transform(raw_df)
    load(transformed_df)


earthquake_pipeline()