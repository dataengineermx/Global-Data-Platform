
import logging
import time
from paths import pipe_logs_path

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

# 1. Definimos un Logger personalizado que cuenta los registrosclass ContadorLogger(logging.Logger):
def __init__(self, name, level=logging.NOTSET):
    super().__init__(name, level)
     # Diccionario para almacenar el conteo por cada nivel
    self.conteos = {"DEBUG": 0, "INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}

def handle(self, record):
    # Cada vez que se procesa un registro, incrementamos su contador si el nivel existe
    if record.levelname in self.conteos:
        self.conteos[record.levelname] += 1
    return super().handle(record)
        
def obtener_resumen(self):
    # Devuelve el total acumulado y el desglose por tipo
    total = sum(self.conteos.values())
    return {"total": total, "detalles": self.conteos}


'''
# 2. Registramos nuestra clase personalizada en el sistema de logging de Python
logging.setLoggerClass(ContadorLogger)
def configurar_mi_logger(nombre_modulo):
    logger = logging.getLogger(nombre_modulo)
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        formato = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        
        manejador_archivo = logging.FileHandler(pipe_logs_path/'app.log')
        manejador_archivo.setFormatter(formato)
        logger.addHandler(manejador_archivo)
        
    return logger
'''