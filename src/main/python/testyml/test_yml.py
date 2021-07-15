# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file test_yml.py
# @description test_yml
# @author WcJun
# @date 2021/07/15
# ---------------------------------------------
import os

import pytest
import requests

from src.main.python.util.yml_reader import YmlReader

# yaml_directory_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
yml_path = os.path.join(os.getcwd() + '{}src{}main{}resources{}test_yml.yml'.format(os.sep, os.sep, os.sep, os.sep))
reader = YmlReader(yml_path)
content = reader.read_yml()


class TestRefreshAccessToken:
    """
    refresh access token
    """

    @pytest.mark.parametrize('context', content)
    def test_refresh_access_token(self, context):
        """
        do refresh access token
        """
        url = context['request']['url']
        parameters = context['request']['parameters']
        response = requests.get(url=url, params=parameters)
        print(response.text)
