import logging
import pathlib

audit_dir = pathlib.Path('logs')
audit_dir.mkdir(exist_ok=True)

log_file = audit_dir/'suite.log'

logger = logging.getLogger('Talento_Tech')
logger.setLevel(logging.INFO)


if not logger.handlers:
    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8") #el mode "a" escribe sobre el mismo archivo y no crea otro

    formatter = logging.Formatter(
        format="%(asctime)s %(levelname)s %(name)s: %(message)s", datefmt='%Y-%m-%d %H:%M:%S'
        #"%(asctime)s %(levelname)s %(name)s %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

#Aun no se implemento clase 26/11 a los 40m aprox