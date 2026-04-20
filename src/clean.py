


import pandas as pd 
from loguru import logger


def cleaning_data(df_brute : pd.DataFrame, file : str) -> pd.DataFrame:
    """Cette fonction se charge du néttoyage des données brites extrait"""
    logger.info("Début du néttoyage des données brutes")

    df_rh = df_brute.copy()
    logger.info('Copie des données brutes reçu effectué')

    column_text = ['full_name', 'position', 'city', 'performance_rating']
    df_rh[column_text] = df_rh[column_text].apply(lambda x: x.str.strip().str.title())

    df_rh['department'] = df_rh['department'].str.strip().str.upper()

    df_rh['experience_years'] = pd.to_numeric(df_rh['experience_years'], errors='coerce').fillna(0).astype(int)
    #pd.to_numeric() tente la conversion
    #errors='coerce' transforme les valeurs invalides en NaN au lieu de planter

    df_rh['hire_date'] = pd.to_datetime(df_rh['hire_date'], format='mixed', dayfirst=True, errors='coerce')

    df_rh['salary'] = pd.to_numeric(
        df_rh['salary']
        .str.replace('€', '', regex=False)
        .str.replace(' ', '', regex=False),
        errors='coerce'
    ).fillna(0).astype(int)
    
    df_rh['bonus'] = pd.to_numeric(
        df_rh['bonus']
        .str.replace('%', '', regex=False)
        .str.replace(' ', '', regex=False),
        errors='coerce'
    ).fillna(0) / 100

    logger.info("Données Brutes néttoyées avec succée")
    df_rh.to_csv(file, index=False)
    return df_rh
