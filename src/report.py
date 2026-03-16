

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
                        'seuil_key' : 'bonus'
                        },

                    'salary': {
                        'colonne': 'salary',
                        'seuil_key': 'salary'
                        },

                    'bonus_amount': {
                        'colonne': 'bonus_amount',
                        'seuil_key': 'bonus_amount'
                        },

                    'total_compensation': {
                        'colonne': 'total_compensation',
                        'seuil_key': 'total_compensation'
                        },

                    'annuel_compensation': {
                        'colonne': 'annuel_compensation',
                        'seuil_key': 'annuel_compensation'
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
            year_numb_cols = ['year_in_company', 'year_in_company_mean', 'experience_years', 'experience_years_mean']
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


            if name == 'Données Par Département':
                logger.info(f'Début de la création du graphique pour la feuille {name}')
                chart_col = workbook.add_chart({'type' : 'column'})
                chart_line = workbook.add_chart({'type' : 'line'})
                departement_col = data.columns.get_loc('department')
                sal_col = data.columns.get_loc('salary')
                bon_col = data.columns.get_loc('bonus_amount')
                total_col = data.columns.get_loc('total_compensation') 

                chart_col.add_series(
                    {
                        'name' : 'total_compensation',
                        'categories' : [name, 1, departement_col, len(data), departement_col],
                        'values' : [name, 1, total_col, len(data), total_col]
                    }
                )


                chart_col.add_series(
                    {
                        'name' : 'salary',
                        'categories' : [name, 1, departement_col, len(data), departement_col],
                        'values' : [name, 1, sal_col, len(data), sal_col]
                    }
                )

                chart_line.add_series(
                    {
                        'name' : 'bonus_amount',
                        'categories' : [name, 1, departement_col, len(data), departement_col],
                        'values' : [name, 1, bon_col, len(data), bon_col],
                        'y2_axis' : True
                    }
                )


                chart_col.combine(chart_line)
                worksheet.insert_chart(1, data.shape[1] + 1, chart_col)

                logger.info(f'Graphique crée avec succée pour la feuille {name}')
            
            if name == 'Données Par Level':
                logger.info(f'Début de la création du graphique pour la feuille {name}')
                chart_col = workbook.add_chart({'type' : 'column'})
                chart_line = workbook.add_chart({'type' : 'line'})
                level_col = data.columns.get_loc('level')
                annuel_col = data.columns.get_loc('annuel_compensation_mean')
                exp_col = data.columns.get_loc('experience_years_mean')

                chart_col.add_series(
                    {
                        'name' : 'annuel_compensation_mean',
                        'categories' : [name, 1 , level_col, len(data), level_col],
                        'values' : [name, 1, annuel_col, len(data), annuel_col]
                    }
                )

                chart_line.add_series(
                    {
                        'name' : 'experience_years_mean',
                        'categories' : [name, 1, level_col, len(data), level_col],
                        'values' : [name, 1, exp_col, len(data), exp_col],
                        'y2_axis' : True
                    }
                )

                chart_col.combine(chart_line)
                chart_col.set_title({'name' : 'salaires par Niveau'})
                worksheet.insert_chart(1, data.shape[1] + 1, chart_col)
                logger.info(f'Graphique crée avec succée pour la feuille {name}')

            if name == 'Données Par ancienneté':
                logger.info(f'Début de la création du graphique pour la feuille {name}')
                chart_line = workbook.add_chart({'type' : 'line'})
                chart_col = workbook.add_chart({'type' : 'column'})
                anc_col = data.columns.get_loc('anciennete')
                bonus_col = data.columns.get_loc('bonus_amount')  
                sal_col = data.columns.get_loc('salary')
                total_col = data.columns.get_loc('total_compensation')

                chart_line.add_series(
                    {
                        'name' : 'bonus_amount',
                        'categories' : [name, 1, anc_col, len(data), anc_col],
                        'values' : [name, 1, bonus_col, len(data), bonus_col]
                    }
                )

                chart_col.add_series(
                    {
                        'name' : 'total_compensation',
                        'categories' : [name, 1, anc_col, len(data), anc_col],
                        'values' : [name, 1, total_col, len(data), total_col],
                        'y2_axis' : True
                    }
                )

                chart_col.add_series(
                    {
                        'name' : 'salary',
                        'categories' : [name, 1, anc_col, len(data), anc_col],
                        'values' : [name, 1, sal_col, len(data), sal_col],
                        'y2_axis' : True
                    }
                )

                chart_line.combine(chart_col)
                chart_line.set_title({'name' : 'Salaires/Bonus -> ancienneté'})
                worksheet.insert_chart(1, data.shape[1] + 1, chart_line)
                logger.info(f'Graphique crée avec succée pour la feuille {name}')
            
            if name == 'Données Top_Salaire_Département':
                logger.info(f'Début de la création du graphique pour la feuille {name}')
                chart_pie = workbook.add_chart({'type' : 'pie'})
                department_col = data.columns.get_loc('department')
                total_col = data.columns.get_loc('total_compensation')

                chart_pie.add_series(
                    {
                        'name' : 'total_compensation',
                        'categories' : [name, 1, department_col, len(data), department_col],
                        'values' : [name, 1, total_col, len(data), total_col],
                        'data_labels' : {'percentage' : True, 'category' : True, 'position' : 'outside_end'}
                    }
                )

                chart_pie.set_legend({'position' : 'none'})
                chart_pie.set_title({'name' : 'Top Salaies par Département'})
                worksheet.insert_chart(1, data.shape[1] + 1, chart_pie)
                logger.info(f'Graphique crée avec succée pour la feuille {name}')

            if name == 'Données Par performance_rating':
                logger.info(f'Début de la création du graphique pour la feuille {name}')
                chart_col = workbook.add_chart({'type': 'column'})
                perf_col = data.columns.get_loc('performance_rating')
                salaire_col = data.columns.get_loc('salary')
                
                chart_col.add_series({
                    'name': 'Salaire moyen',
                    'categories': [name, 1, perf_col, len(data), perf_col],
                    'values': [name, 1, salaire_col, len(data), salaire_col]
                })
                chart_col.set_title({'name': 'Salaire par niveau de performance'})
                worksheet.insert_chart(1, data.shape[1] + 1, chart_col)
                logger.info(f'Graphique crée avec succée pour la feuille {name}')


                    
                
    print('Thanks')
