

from loguru import logger
import pandas as pd
import xlsxwriter
from typing import Dict



def repporting_excel(file_excel, multi_onglets : Dict[str , pd.DataFrame]):
    with pd.ExcelWriter(file_excel, engine='xlsxwriter') as writer:
        workbook = writer.book

        base_style = {
            'border' : 1,
            'align' : 'center',
            'valign' : 'center'
        }
        data_format = workbook.add_format(base_style)

        header_format = workbook.add_format({
            **base_style,
            'bold' : True,
            'bg_color' : '#4F81BD',
            'font_color' : 'white'
        })
        

        money_fmt = workbook.add_format({**base_style, 'num_format': '#,##0" €"'})
        prcnt_fmt = workbook.add_format({**base_style, 'num_format': '0  %'})
        #liste = ['salary', 'bonus', 'total_compensation', 'bonus_amount']
        for name, data in multi_onglets.items():
            data.to_excel(writer, sheet_name=name, index=False)
            worksheet = writer.sheets[name]
            for col_numb, value in enumerate(data.columns.values):
                worksheet.write(0, col_numb, value, header_format)
            worksheet.freeze_panes(1, 0)
            cols_monetaires = ['salary', 'total_compensation', 'bonus_amount']
            cols_percent = ['bonus']
            for i, column in enumerate(data.columns):
                column_width = data[column].astype(str).str.len().max()
                column_width = max(column_width, len(column)) + 3
                #if 'salary' in column or 'total_compensation' in column or 'bonus_amount' in column:
                if column in cols_monetaires:
                    worksheet.set_column(i, i, column_width, money_fmt)
                elif column in cols_percent:
                    worksheet.set_column(i, i, column_width, prcnt_fmt)
                else:
                    worksheet.set_column(i, i, column_width, data_format)

    print('Thanks')
