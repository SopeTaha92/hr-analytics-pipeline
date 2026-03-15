





import pandas as pd 
from loguru import logger


def analysis_by_anciennete(df_rh : pd.DataFrame):
    """Cette fonction se charge d'effectuer des analyses par ancienneté"""
    logger.info("Début des analyses par ancienneté")
    df_rh_anciennete = (
        df_rh.groupby('anciennete')
        .agg(
            {
                'employee_id' : 'count',
                'salary' : 'mean',
                'bonus_amount' : 'mean',
                'total_compensation' : 'mean',
                'annuel_compensation' : 'mean'
            }
        )
        .round(2)
        .reset_index()
    ) 
    logger.info("Analyse par ancienneté effeectue avec succée")
    return df_rh_anciennete
        