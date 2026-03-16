


from pathlib import Path
from datetime import datetime
from loguru import logger

TODAY = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
MAX_RETRIES = 3
DELAY = 1
TOP_SALAIRE_DEPARTEMENT = 1

#BRUTE_DATA_FILE = Path('data/raw/donnee_brute_rh.csv')
BRUTE_DATA_FILE = Path('data/raw/donnees_rh_1000_lignes.csv')
BRUTE_DATA_CLEAN_DIR = Path('data/processed')
BRUTE_DATA_CLEAN_DIR.mkdir(parents=True, exist_ok=True)
BRUTE_DATA_CLEAN_FILE = BRUTE_DATA_CLEAN_DIR / "donnee_brute_rh_clean.csv"

LOG_DIR = Path('logs')
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / f"logging_file_{TODAY}.log"

EXCEL_DIR = Path('Output_excel')
EXCEL_DIR.mkdir(parents=True, exist_ok=True)
EXCEL_FILE = EXCEL_DIR / f"DONNÉES_RH_BRUTES_{TODAY}.xlsx"




# Dans config.py pour ce projet
EXCEL_FORMATTING_RH = {

    'salary': {
        'min_orange': 45000,
        'max_orange': 60000,
        'green_value': 60000,
        'red_value': 45000
    },

    'bonus_amount' : {
        'min_orange': 5000,
        'max_orange': 10000,
        'green_value': 10000,
        'red_value': 5000
        },

    'anciennete': {
        'anciennete' : {'Junior': 3, 'Sénior': 7, 'Ancien': 10}
    },

    'bonus' : {
        'red_value' : 0.10,
        'min_orange' : 0.10,
        'max_orange' : 0.15,
        'green_value' : 0.15
    },  

    'total_compensation' : {
        'min_orange': 50000,
        'max_orange': 70000,
        'green_value': 70000,
        'red_value': 50000
    },

    'annuel_compensation' : {
        'min_orange': 600000,
        'max_orange': 800000,
        'green_value': 800000,
        'red_value': 600000
    }
}

COULEURS_EXCEL_RH = {
    'vert': '#C6EFCE',
    'rouge': '#FFC7CE',
    'orange': '#FFEB9C',
    'header': '#4472C4',  # Bleu professionnel pour RH
    'expert': '#9BC2E6',   # Bleu clair
    'senior': '#A9D08E',   # Vert
    'junior': '#FFD966'    # Jaune
}