


import sys

from loguru import logger
import pandas as pd
import time



def extracting_data(file : str, max_retries : int, delay : int):
    """Cette fonction se charge de l'extraction des données brutes depuis la source ici un fichier csv"""
    logger.info("Début de l'extraction des données brutes depuis le fichier csv source")
    for retry in range(max_retries):
        try:
            df_brute = pd.read_csv(file)
            logger.success("Données brutes extrait avec succée")
            return df_brute
        except FileNotFoundError as e:
            logger.error(f"Erreur lors de la tentative {retry+1} / {max_retries} d'extraction des données brutes ")
            if retry < max_retries - 1:
                logger.info(f'Nouvelle tentative dans {delay} secondes')
                time.sleep(delay)
                delay *= 2
    logger.critical(f"Echec total aprés {max_retries} tentatives")
    sys.exit("Arret complet du programme aprés les echecs")

    return df_brute
