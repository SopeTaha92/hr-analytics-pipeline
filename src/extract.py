


import sys
from loguru import logger
import pandas as pd
import time
import psycopg2
from config import DB_CONFIG, TABLE_NAME, MAX_RETRIES, DELAY



def extracting_data(max_retries : int = MAX_RETRIES , delay : int = DELAY) -> pd.DataFrame:
    """Cette fonction se charge de l'extraction des données brutes depuis la source ici un fichier csv"""
    logger.info("Début de l'extraction des données brutes depuis le fichier csv source")
    for retry in range(max_retries):
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            logger.info('testing connection !')
            df_brute = pd.read_sql(f"SELECT * FROM {TABLE_NAME};", conn)
            logger.info("✅ Connexion réussie !")
            conn.close()
            logger.success("Données brutes extrait avec succée")
            return df_brute
        except Exception as e:
            logger.error(f"Erreur lors de la tentative {retry+1} / {max_retries} d'extraction des données brutes : {e}")
            if retry < max_retries - 1:
                logger.info(f'Nouvelle tentative dans {delay} secondes')
                time.sleep(delay)
                delay *= 2
    logger.critical(f"Echec total aprés {max_retries} tentatives")
    sys.exit("Arret complet du programme aprés les echecs")

    
