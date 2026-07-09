from dotenv import load_dotenv
import os
import sys
import psycopg
import logging
import pandas as pd
from src.monitor import logging_config
from src.monitor import job_monitor
from src.utils.paths import data_clean_path
from src.stringIObuffer.earthquakes_buffer import dataframe_to_buffer



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger(__name__)


file_path=data_clean_path
target_table="earthquakes"

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

def bulk_load_csv_to_postgres(file_path: str, target_table: str) -> None:
    """Loads a CSV into PostgreSQL using streaming COPY protocols with transaction rollback."""
    csv_path = file_path
    
    if not csv_path.is_file():
        logger.error(f"Target execution file path does not exist: {file_path}")
        return

    conn_str = get_db_connection_string()
    
    logger.info(f"Initiating bulk upload of {csv_path.name} into table '{target_table}'")

    # Context manager handles implicit database connection closures
    try:
        with psycopg.connect(conn_str) as conn:
            # Explicitly manage transaction isolation if required, default is autocommit=False
            with conn.cursor() as cur:
                
                # Open CSV file stream with strict encoding parameters
                with open(csv_path, mode='r', encoding='utf-8', errors='strict') as f:
                    
                    # Construct optimized COPY command (explicitly list target columns if mismatched)
                    copy_query = f"COPY {target_table} FROM STDIN WITH (FORMAT csv, HEADER true)"
                    
                    # FREEZE reduces WAL (Write-Ahead Logging) overhead for newly created or empty tables
                    with cur.copy(copy_query) as copy:
                        while chunk := f.read(65536):  # Optimized 64KB memory chunk blocks
                            copy.write(chunk)
                            
            # The context manager automatically issues a COMMIT here if no exceptions occurred.
            logger.info("Bulk copy pipeline execution completed successfully. Changes committed.")
            
    except psycopg.OperationalError as db_err:
        logger.critical(f"Database network connection failed: {db_err}")
    except psycopg.DataError as data_err:
        logger.error(f"Data type mismatch constraint failure during streaming COPY operation: {data_err}")
    except Exception as general_err:
        # Context manager automatically triggers a ROLLBACK before entering this block
        logger.error(f"Transaction aborted. Pipeline safely rolled back due to unhandled exception: {general_err}")

if __name__ == "__main__":
    # In production, pass these via arguments, task runner orchestration (Airflow), or configurations
    CSV_FILE = dataframe_to_buffer
    TABLE_NAME = target_table
    
    bulk_load_csv_to_postgres(CSV_FILE, TABLE_NAME)

