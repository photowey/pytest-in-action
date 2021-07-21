# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file excel_reader.py
# @description excel_reader
# @author WcJun
# @date 2021/07/21
# ---------------------------------------------


import pandas as pd


class ExcelReader(object):
    """
    read excel
    """

    def __init__(self, excel_file: str):
        self.excel_file = excel_file

    def read_excel(self, sheet_name='sheet1', index_col=1, fillna=True, engine='openpyxl') -> list:
        """
        read excel by pandas lib, use openpyxl engine.
        """
        try:
            with open(self.excel_file, 'rb') as file_bin:
                data = pd.read_excel(file_bin, sheet_name=sheet_name, index_col=index_col, engine=engine)
                if fillna:
                    data.fillna('', inplace=True)
                value_list = data.values.tolist()
                return value_list
        except FileNotFoundError as e:
            print('file not found! {}'.format(e))
        except TypeError as t:
            print('file type error! {}'.format(t))
