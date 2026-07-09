from dotenv import load_dotenv
import sys
import os
import psycopg
import logging
import pandas as pd
from src.monitor import logging_config
from src.monitor import job_monitor
from src.transform.earthquake_transform import dataframe_to_buffer


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger(__name__)


from src.transform.earthquake_transform import (
    earthquake_transform,
    dataframe_to_buffer,
)

df = earthquake_transform()
buffer = dataframe_to_buffer(df)


def get_db_connection_string() -> str:
    """Builds a secure psycopg connection string from system environments."""
    try:
        return psycopg.conninfo.make_conninfo(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

    except KeyError as e:
        logger.critical(f"Missing required environment deployment variable: {e}")
        sys.exit(1)

try:
    with psycopg.connect(get_db_connection_string()) as conn:
        with conn.cursor() as cur:
            with cur.copy(
                """COPY earthquakes (eventtype, status, magnitude, place, longitude, latitude, depth, time) FROM STDIN WITH CSV HEADER"""
            ) as copy:
                copy.write(buffer.getvalue())
except psycopg.OperationalError as db_err:
    logger.critical(f"Database network connection failed: {db_err}")
except psycopg.DataError as data_err:
    logger.error(f"Data type mismatch constraint failure during streaming COPY operation: {data_err}")
except Exception as general_err:
    # Context manager automatically triggers a ROLLBACK before entering this block
    logger.error(f"Transaction aborted. Pipeline safely rolled back due to unhandled exception: {general_err}")