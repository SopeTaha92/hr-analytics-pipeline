


import pandas as pd 
from loguru import logger


def analysis_by_department(df_rh : pd.DataFrame):
    df_rh_category = (
        df_rh.groupby('department')
        .agg(
            {
                'salary' : 'mean',
                'bonus_amount' : 'mean',
                'total_compensation' : 'mean',
                'experience_years' : 'mean',
                'year_in_company' : 'mean',
                'performance_rating' : lambda x: x.mode().iloc[0] if not x.mode().empty else 'N/A'
            }
        ).round(2)
        .reset_index() 
    ) 




    pass