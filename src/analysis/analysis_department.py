


import pandas as pd 
from loguru import logger


def analysis_by_department(df_rh : pd.DataFrame):
    """Cette fonction se charge d'effectuer des analyses par departement"""
    logger.info("Début des analyses par département")
    df_rh_department = (
        df_rh.groupby('department')
        .agg(
            {
                'employee_id' : 'count',
                'salary' : 'mean',#   ['mean', 'min', 'max']
                'bonus_amount' : 'mean',
                'total_compensation' : 'mean',
                'experience_years' : 'mean',
                'year_in_company' : 'mean',
                #'performance_rating' : lambda x: x.mode().iloc[0] if not x.mode().empty else 'N/A'
                'annuel_compensation' : 'mean'
            }
        )
        .round(2)
        .reset_index()
        
    ) 
    logger.info("Analyse par département effeectue avec succée")
    return df_rh_department 