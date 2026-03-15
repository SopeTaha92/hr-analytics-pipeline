


import pandas as pd 
from loguru import logger 


def analysis_by_top_salaries_par_departement(df_rh: pd.DataFrame, top_n: int):
    """Trouve les top N salaires dans chaque département."""
    logger.info(f"Début de la collecte des {top_n} top salaires par département")
    
    # Version avec nlargest (plus explicite)
    df_rh_top_salaries_par_departement = (
        df_rh.sort_values('total_compensation', ascending=False)
        .groupby('department')
        .head(top_n)
        [['department', 'full_name', 'total_compensation', 'level']]
        .sort_values(by=['department', 'total_compensation'], ascending=[True, False])
    )
    
    logger.success(f"Collecte des {top_n} top salaires par département effectuée avec succès")
    return df_rh_top_salaries_par_departement