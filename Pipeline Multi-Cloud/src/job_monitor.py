import logging
import uuid
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)


class LoadMonitor:

    def __init__(self, process_name):
        self.run_id = str(uuid.uuid4())[:8]
        self.process_name = process_name
        self.start_time = None

    def start(self):
        self.start_time = datetime.now()

        logging.info(
            f"RUN_ID={self.run_id} | "
            f"PROCESS={self.process_name} | "
            f"STATUS=STARTED"
        )

    def success(self, records):
        end_time = datetime.now()

        duration = (
            end_time - self.start_time
        ).total_seconds()

        logging.info(
            f"RUN_ID={self.run_id} | "
            f"PROCESS={self.process_name} | "
            f"STATUS=SUCCESS | "
            f"RECORDS={records} | "
            f"DURATION={duration:.2f}s"
        )

    def failed(self, error):
        end_time = datetime.now()

        duration = (
            end_time - self.start_time
        ).total_seconds()

        logging.error(
            f"RUN_ID={self.run_id} | "
            f"PROCESS={self.process_name} | "
            f"STATUS=FAILED | "
            f"ERROR={type(error).__name__} | "
            f"MESSAGE={error} | "
            f"DURATION={duration:.2f}s"
        )