import logging
import os
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_FOLDER_PATH = os.path.join(os.getcwd(),'Logs')
os.makedirs(LOG_FOLDER_PATH,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_FOLDER_PATH,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s %(name)s %(lineno)s %(message)s"
)