


from pathlib import Path
from datetime import datetime
from loguru import logger

TODAY = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
MAX_RETRIES = 3
DELAY = 1

BRUTE_DATA_FILE = Path('data/raw/donnee_brute_rh.csv')
BRUTE_DATA_CLEAN_DIR = Path('data/processed')
BRUTE_DATA_CLEAN_DIR.mkdir(parents=True, exist_ok=True)
BRUTE_DATA_CLEAN_FILE = BRUTE_DATA_CLEAN_DIR / "donnee_brute_rh_clean.csv"

LOG_DIR = Path('logs')
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / f"logging_file_{TODAY}.log"

EXCEL_DIR = Path('Output_excel')
EXCEL_DIR.mkdir(parents=True, exist_ok=True)
EXCEL_FILE = EXCEL_DIR / f"DONNÉES_RH_BRUTES_{TODAY}.xlsx"