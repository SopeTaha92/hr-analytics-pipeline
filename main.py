



from config import LOG_FILE, BRUTE_DATA_FILE, EXCEL_FILE, MAX_RETRIES, DELAY

from src import logging_file
from src import extracting_data, cleaning_data, add_features, repporting_excel


logging_file(LOG_FILE)
brute_data = extracting_data(BRUTE_DATA_FILE, MAX_RETRIES, DELAY)
clean_data = cleaning_data(brute_data)
complet_data = add_features(clean_data)





print(f"\n{brute_data}")
print(f"\n{complet_data}")

onglets = {
    'Données Brutes' : brute_data,
    'Données Néttoyées au Complet' : complet_data
    #'Données Salaires Par Catégories' : df_rh_category
}
















"""


import os 
import pandas as pd 
import numpy as ny
from datetime import datetime
from pathlib import Path

today = datetime.now().strftime('%d-%m-%Y_%H-%M')
dir_path = Path(__file__).parent
os.makedirs(dir_path, exist_ok=True)
file = dir_path / f"exo_2_refait_{today}.xlsx"







data_rh = {
    'employee_id': ['EMP-001', 'EMP-002', 'EMP-003', 'EMP-004', 'EMP-005', 'EMP-006', 'EMP-007', 'EMP-008', 'EMP-009', 'EMP-010'],
    'full_name': ['alice martin', 'BOB DUPONT', 'charlie legrand', 'DIANA ROY', 'EVELYN TREMBlAY', 'FRANK KLEIN', 'GRACE LEROY', 'HENRY GAUTHIER', 'IVANA PETROV', 'JACK WILSON'],
    'department': ['IT', 'MARKETING', 'IT', 'SALES', 'HR', 'IT', 'MARKETING', 'SALES', 'IT', 'FINANCE'],
    'position': ['Data Analyst', 'Marketing Manager', 'Software Engineer', 'Sales Rep', 'HR Specialist', 'DevOps Engineer', 'Content Manager', 'Sales Director', 'Data Scientist', 'Financial Analyst'],
    'salary': ['45000€', '52000', '58000€', '38000', '42000€', '62000', '48000€', '65000', '70000€', '55000'],
    'experience_years': ['3', '5', '7', '2', '4', '8', '6', '10', '9', '5'],
    'hire_date': ['2021-03-15', '2019-06-20', '2017-11-10', '2022-01-08', '2020-08-25', '2016-04-12', '2018-09-30', '2014-07-18', '2015-12-01', '2019-03-22'],
    'city': ['paris', 'LYON', 'MARSEILLE', 'LILLE', 'TOULOUSE', 'BORDEAUX', 'NICE', 'STRASBOURG', 'MONTPELLIER', 'RENNES'],
    'performance_rating': ['A', 'B', 'A', 'C', 'B', 'A', 'B', 'A', 'A', 'B'],
    'bonus': ['10%', '8%', '12%', '5%', '7%', '15%', '9%', '18%', '20%', '10%']
}

df_rh_brute = pd.DataFrame(data_rh)
print("📊 DONNÉES RH BRUTES :")
print(df_rh_brute)
df_rh = df_rh_brute.copy()

column_text = ['full_name', 'position','city', 'performance_rating']

df_rh[column_text] = df_rh[column_text].apply(lambda x: x.str.strip().str.title())

df_rh['department'] = df_rh['department'].str.upper()

df_rh['experience_years'] = df_rh['experience_years'].astype(int)

df_rh['salary'] = (
    df_rh['salary']
    .str.replace('€', '', regex=False)
    .str.replace(' ', '', regex=False)
    .replace('', 0, regex=False)
    .astype(int)
    .round(2)
)

df_rh['hire_date'] = pd.to_datetime(
    df_rh['hire_date'],
    format='mixed',
    dayfirst=True,
    errors='coerce' 
)     #'bonus_amount' 'total_compensation : Salaire + Bonus'

df_rh['bonus'] = (
    df_rh['bonus']
    .str.replace('%', '', regex=False)
    .str.replace(' ', '', regex=False)
    .astype(float) / 100
)

df_rh['bonus_amount'] = (df_rh['salary'] * df_rh['bonus']).round(2)

df_rh['total_compensation'] = df_rh['salary'] + df_rh['bonus_amount']

date_now = datetime.now()
#print(date_now)
df_rh['years_in_company'] = ((date_now - df_rh['hire_date']).dt.days / 365.25).round(1)

df_rh_departement = (
    df_rh.groupby('department')
    .agg(
        {
            'total_compensation' : 'mean',
            'years_in_company' : 'mean',
            'experience_years' : 'mean',
            'performance_rating' : lambda x: x.mode().iloc[0] if not x.mode().empty else 'N/A'
        }
    ).round(1)
).reset_index()

df_rh['hire_date'] = df_rh['hire_date'].dt.date

print(f"\n{df_rh}\n{df_rh_departement}")

onglets = {
    'Salaires Brutes' : df_rh_brute,
    'Salaires nettoyés' : df_rh,
    'Statistiques par département' : df_rh_departement
}
with pd.ExcelWriter(file, engine='xlsxwriter') as writer:
    for name, data in onglets.items():
        data.to_excel(writer, sheet_name=name, index=False)
        worksheet = writer.sheets[name]
        for i, column in enumerate(data.columns):
            column_width = data[column].astype(str).str.len().max()
            column_width = max(column_width, len(column)) + 3
            worksheet.set_column(i, i, column_width)

print(f"Thanks Fichier Multi-onglets crée avec succé à : {file}")






with pd.ExcelWriter(file, engine='xlsxwriter') as writer:
    for name, data in onglets.items():
        data.to_excel(writer, sheet_name=name, index=False)
        worksheet = writer.sheets[name]
        for i, col in enumerate(data.columns):
            col_w = data[col].astype(str).str.len().max()
            col_w = max(col_w, len(col)) + 3 
            worksheet.set_column(i, i, col_w)












Explication de la ligne lambda
Comme Pandas n'a pas de fonction 'mode' intégrée en texte (contrairement à 'mean'), on utilise une petite fonction personnalisée (lambda) :

x.mode() : Cherche la valeur la plus fréquente (ex: "B").

.iloc[0] : Prend la première valeur (au cas où il y aurait deux notes à égalité).

if not x.mode().empty : Évite que le code plante si un département n'a aucune note remplie.


"""



""""

with pd.ExcelWriter(file, engine='xlsxwriter') as writer:
    workbook = writer.book
    base_style = {
        'align' : 'center',
        'valign' : 'center',
        'border' : 1
    }
    data_format = workbook.add_format(base_style)
    head_form = workbook.add_format({
        **base_style,
        'bodl' : True,
        'bg_color' : '#4F81BD',
        'font_color' : 'white'
    })

    money_format = workbook.add_format({**base_style, 'num_format' : '#,##0" £"'})
    perct_format = workbook.add_format({**base_style, 'num_format' : '0 %'})
    
    for name, data in onglets.items():
        data.to_excel(writer, sheet_name=name, index=False)
        worksheet = writer.sheets[data]
        for column_numb, value in enumerate(data.columns.values):
            worksheet.writter(0, column_numb, value, head_form)
        worksheet.freeze_panes(1,0)
        for i, column in enumerate(data.columns):
            col_m = ['salary', 'total_compensation', 'bonus_amount']
            col_p = ['bonus']
            column_width = max(data[column].astype(str).str.len().max, len(column)) + 3
            if col_m in column:
                worksheet.set_column(i, i, column_width, money_format)
            elif col_p in column:
                worksheet.set_column(i, i, column_width, perct_format)
            else:
                worksheet.set_column(i, i, column_width, data_format)






"""