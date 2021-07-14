# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file test_yml.py
# @description test_yml
# @author WcJun
# @date 2021/07/15
# ---------------------------------------------
import pytest
import requests

from src.main.python.util.yml_reader import YmlReader

resources = '../../resources'

reader = YmlReader('{}/test_yml.yml'.format(resources))
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
        print(context)
        url = context['request']['url']
        parameters = context['request']['parameters']
        response = requests.get(url=url, params=parameters)
        print(response.text)
