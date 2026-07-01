from logging_config import config_my_logger
from logging_config import handle
from logging_config import obtener_resumen
from logging_config import configurar_mi_logger
from logging_config import elapsedtime
logger = config_my_logger("JOB_001")

logger.info("Inicio del proceso")
logger.error("Error en la carga")
elapsedtime
