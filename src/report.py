

from loguru import logger
import pandas as pd
import xlsxwriter
from typing import Dict
import config


def repporting_excel(file_excel, multi_onglets : Dict[str , pd.DataFrame]):
    with pd.ExcelWriter(file_excel, engine='xlsxwriter') as writer:
        workbook = writer.book

        header = config.COULEURS_EXCEL_RH['header']
        rouge = config.COULEURS_EXCEL_RH['rouge']
        orange = config.COULEURS_EXCEL_RH['orange']
        vert = config.COULEURS_EXCEL_RH['vert']

        red_format = workbook.add_format({'bg_color' : rouge})
        orange_format = workbook.add_format({'bg_color' : orange})
        green_format = workbook.add_format({'bg_color' : vert})


        base_style = {
            'border' : 1,
            'align' : 'center',
            'valign' : 'center'
        }
        data_format = workbook.add_format(base_style)

        header_format = workbook.add_format({
            **base_style,
            'bold' : True,
            'italic' : True,
            'bg_color' : header,
            'font_color' : 'white'
        })
        


        money_fmt = workbook.add_format({**base_style, 'num_format': '#,##0" €"'})
        prcnt_fmt = workbook.add_format({**base_style, 'num_format': '0  %'})
        year_numb_fmt = workbook.add_format({**base_style, 'num_format' : '0" ans"'})
        
        COLONNE_FORMATER = {
                    'bonus' : {
                        'colonne' : 'bonus',
                        'seuil_key' : 'bonus',
                        'type' : 'percent'
                        },

                    'salary': {
                        'colonne': 'salary',
                        'seuil_key': 'salary',
                        'type': 'monetary'
                        },

                    'bonus_amount': {
                        'colonne': 'bonus_amount',
                        'seuil_key': 'bonus_amount',
                        'type': 'monetary'
                        },

                    'total_compensation': {
                        'colonne': 'total_compensation',
                        'seuil_key': 'total_compensation',
                        'type': 'monetary'
                        },

                    'annuel_compensation': {
                        'colonne': 'annuel_compensation',
                        'seuil_key': 'annuel_compensation',
                        'type': 'monetary'
                        }        
                }
        #liste = ['salary', 'bonus', 'total_compensation', 'bonus_amount']
        for name, data in multi_onglets.items():
            data.to_excel(writer, sheet_name=name, index=False)
            worksheet = writer.sheets[name]
            for col_numb, value in enumerate(data.columns.values):
                worksheet.write(0, col_numb, value, header_format)
            worksheet.freeze_panes(1, 0)
            cols_monetaires = ['salary', 'total_compensation', 'bonus_amount', 'annuel_compensation', 'salary_mean', 'salary_min', 'salary_max', 'total_compensation_mean', 'annuel_compensation_mean', 'bonus_amount_mean']
            cols_percent = ['bonus']
            year_numb_cols = ['year_in_company', 'experience_years']
            for i, column in enumerate(data.columns):
                column_width = data[column].astype(str).str.len().max()
                column_width = max(column_width, len(column)) + 3
                #if 'salary' in column or 'total_compensation' in column or 'bonus_amount' in column:
                if column in cols_monetaires:
                    worksheet.set_column(i, i, column_width, money_fmt)
                elif column in cols_percent:
                    worksheet.set_column(i, i, column_width, prcnt_fmt)
                elif column in year_numb_cols:
                    worksheet.set_column(i, i, column_width, year_numb_fmt)
                else:
                    worksheet.set_column(i, i, column_width, data_format)

            if name == 'Données Néttoyées au Complet':
                logger.info("Application de la mise en forme conditionnelle")

                for config_col in COLONNE_FORMATER.values():
                    col_name = config_col['colonne']
                    seuil_key = config_col['seuil_key']

                    if col_name in data.columns:
                        name_column = data.columns.get_loc(col_name)
                        seuil = config.EXCEL_FORMATTING_RH[seuil_key]

                        worksheet.conditional_format(1, name_column, len(data), name_column, {
                            'type' : 'cell',
                            'criteria' : '<',
                            'value' : seuil['red_value'],
                            'format' : red_format
                        })

                        worksheet.conditional_format(1, name_column, len(data), name_column, {
                            'type' : 'cell',
                            'criteria' : '>',
                            'value' : seuil['green_value'],
                            'format' : green_format
                        })

                        worksheet.conditional_format(1, name_column, len(data), name_column, {
                            'type' : 'cell',
                            'criteria' : 'between',
                            'minimum' : seuil['min_orange'],
                            'maximum' : seuil['max_orange'],
                            'format' : orange_format
                        })

                        logger.debug(f"Format conditionnel appliqué à {col_name}")


                    
                
    print('Thanks')
