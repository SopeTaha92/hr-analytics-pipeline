





import pandas as pd 
from loguru import logger


def analysis_by_performance_rating(df_rh : pd.DataFrame) -> pd.DataFrame:
    """Cette fonction se charge d'effectuer des analyses par performance_rating"""
    logger.info("Début des analyses par performance_rating")
    df_rh_performance_rating = (
        df_rh.groupby('performance_rating')
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
    return df_rh_performance_rating
        