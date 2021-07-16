# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file conftest.py
# @description conftest
# @author WcJun
# @date 2021/07/16
# ---------------------------------------------
import pytest

from src.main.python.logger.pytest_logger import PytestLogger


@pytest.fixture(
    scope='function',
    autouse=False,
    params=['Java0001', 'Python0010', 'Go0101'],
    ids=['J1', 'P2', 'G3'],
    name='global_class_post_processor'
)
def global_fixture(request):
    """
    global_fixture
    """
    print('\nyield::global_fixture::do pre()')
    yield request.param
    print('\nyield::global_fixture::do post()')


@pytest.fixture(
    scope='session',
    autouse=True
)
def logger():
    handler = PytestLogger()
    return handler
