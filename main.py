



import os 
import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
from src import brute_data, excel_generate



today = datetime.now().strftime('%d-%m-%Y_%H_%M')

dir_path = Path(__file__).parent
os.makedirs(dir_path, exist_ok=True)
file = dir_path / "Output_excel" / f"DONNÉES_RH_BRUTES_{today}.xlsx"


df_rh_brute = brute_data()
print("📊 DONNÉES RH BRUTES :")
print(df_rh_brute)


df_rh = df_rh_brute.copy()

column_text = ['full_name', 'position', 'city', 'performance_rating']
df_rh[column_text] = df_rh[column_text].apply(lambda x: x.str.strip().str.title())
df_rh['department'] = df_rh['department'].str.upper()
df_rh['experience_years'] = df_rh['experience_years'].astype(int)
df_rh['hire_date'] = pd.to_datetime(df_rh['hire_date'], format='mixed', dayfirst=True, errors='coerce')
df_rh['salary'] = (
    df_rh['salary']
    .str.replace('€', '', regex=False)
    .str.replace(' ', '', regex=False)
    .replace('', 0, regex=False)
    .astype(int)
)
df_rh['bonus'] = (
    df_rh['bonus']
    .str.replace('%', '', regex=False)
    .str.replace(' ', '', regex=False)
    .astype(float) / 100
).fillna(0)

df_rh['bonus_amount'] = (df_rh['salary'] * df_rh['bonus']).round(2)
df_rh['total_compensation'] = round((df_rh['salary'] + df_rh['bonus_amount']), 2)
df_rh['year_in_company'] = ((datetime.now() - df_rh['hire_date']).dt.days / 365.25).round(1)
df_rh['hire_date'] = df_rh['hire_date'].dt.date

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

print(f"\n{df_rh}")
print(f"\n{df_rh_category}")

onglets = {
    'Données Salaires Brutes' : df_rh_brute,
    'Données Salaires Néttoyées' : df_rh,
    'Données Salaires Par Catégories' : df_rh_category
}

Excel = excel_generate(file, onglets)











"""
