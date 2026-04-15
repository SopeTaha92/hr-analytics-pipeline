


from datetime import datetime
import pandas as pd 
from loguru import logger



def add_features(df_rh : pd.DataFrame) -> pd.DataFrame:
    """Cette fonction s'occupe d'ajouter des colonnes supplémentaires"""
    logger.info("Début de l'ajout des nouvelles colonnes")

    df_rh['level'] = df_rh['experience_years'].apply(lambda x: "Expert" if x > 7 else("Sénior" if x > 4 else "Junior"))
    df_rh['bonus_amount'] = (df_rh['salary'] * df_rh['bonus']).round(2)
    df_rh['total_compensation'] = round((df_rh['salary'] + df_rh['bonus_amount']), 2)
    df_rh['year_in_company'] = ((datetime.now() - df_rh['hire_date']).dt.days / 365.25).round(1)
    df_rh['hire_date'] = df_rh['hire_date'].dt.date

    df_rh['anciennete'] = df_rh['year_in_company'].apply(lambda x: "Ancien" if x > 10 else("Sénior" if x > 7 else "Junior"))
    df_rh['annuel_compensation'] = (df_rh['total_compensation'] * 12).astype(int)

    logger.info("Nouvelles colonnes ajoutés avec succée")
    return df_rh