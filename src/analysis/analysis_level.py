





import pandas as pd 
from loguru import logger


def analysis_by_level(df_rh : pd.DataFrame):
    """Cette fonction se charge d'effectuer des analyses par Level"""
    logger.info("Début des analyses par Level")
    df_rh_level = df_rh.copy()
    df_rh_level = (
        df_rh.groupby('level')
        .agg(
            {
                'employee_id' : 'count',
                'salary' : ['min', 'mean', 'max'],
                'bonus_amount' : 'mean',
                'total_compensation' : 'mean',
                'experience_years' : 'mean',
                'year_in_company' : 'mean',
                'annuel_compensation' : 'mean'
            }
        )
        .round(2)
    ) 

    df_rh_level.columns = ['_'.join(col).strip() for col in df_rh_level.columns.values]
    logger.info("Analyse par Level effeectue avec succée")
    return df_rh_level.reset_index()
        