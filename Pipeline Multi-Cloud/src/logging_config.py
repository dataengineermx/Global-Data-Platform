
import logging
import time


#Get duration of job execution
start = time.time()
elapsedtime = time.time() - start
logging.info(f"Elapsed Time: {elapsedtime:.2f} seconds")


def config_my_logger(logger_jobs):
    # Crear un logger personalizado
    logger = logging.getLogger(logger_jobs)
    logger.setLevel(logging.DEBUG) # Nivel mínimo para registrar
    
    # Evitar que los mensajes se dupliquen si la función se llama varias veces
    if not logger.handlers:
        # Formato del mensaje de log
        format = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        
        # Handler para guardar en archivo
        manage_file = logging.FileHandler('app.log')
        manage_file.setFormatter(format)
        logger.addHandler(manage_file)
        
        # (Opcional) Handler para ver los logs en la consola
        manage_console = logging.StreamHandler()
        manage_console.setFormatter(format)
        logger.addHandler(manage_console)
        
    return logger

# Count number of registrosclass ContadorLogger(logging.Logger):
def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)
        # Diccionario para almacenar el conteo por cada nivel
        self.counts = {"DEBUG": 0, "INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}

def handle(self, record):
   # Cada vez que se procesa un registro, incrementamos su contador si el nivel existe
    if record.levelname in self.counts:
        self.counts[record.levelname] += 1
    return super().handle(record)
        
def obtener_resumen(self):
    # Devuelve el total acumulado y el desglose por tipo
    total = sum(self.counts.values())
    return {"total": total, "details": self.counts}

# 2. Logging

def configurar_mi_logger(count_job):
    logger = logging.getLogger(str(count_job))
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formato = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        )

        manage_file = logging.FileHandler('app.log')
        manage_file.setFormatter(formato)

        logger.addHandler(manage_file)

    return logger