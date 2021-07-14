# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file yml_reader.py
# @description yml_reader
# @author WcJun
# @date 2021/07/15
# ---------------------------------------------


import yaml


class YmlReader:
    """
    yml reader
    """

    def __init__(self, yml_file):
        """
        init yml file
        """
        self.yml_file = yml_file

    def read_yml(self):
        """
        read yml file
        """
        with open(self.yml_file, encoding='utf-8') as f:
            content = yaml.load(f, Loader=yaml.FullLoader)
            return content
