import logging
import uuid
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)


class LoadMonitor:

    def __init__(self, process_name):
        self.run_id = str(uuid.uuid4())[:8]
        self.process_name = process_name
        self.start_time = None
        self.logger = self.get_logger()

    def start(self):
        self.start_time = datetime.now(ZoneInfo("America/Mexico_City"))

        logging.info(
            f"RUN_ID={self.run_id} | "
            f"PROCESS={self.process_name} | "
            f"STATUS=STARTED"
        )

    def success(self, records):
        end_time = datetime.now(ZoneInfo("America/Mexico_City"))

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
        end_time = datetime.now(ZoneInfo("America/Mexico_City"))

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

    def get_logger(self):

        # Crear carpeta logs si no existe
        Path("logs").mkdir(exist_ok=True)
        logger = logging.getLogger(self.process_name)
        logger.setLevel(logging.INFO)

        # Evita agregar handlers duplicados
        if not logger.handlers:

            formatter = logging.Formatter(
                '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
            )

            file_handler = logging.FileHandler(
                f"logs/{self.process_name}.log",
                encoding="utf-8"
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger