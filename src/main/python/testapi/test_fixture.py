# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file test_fixture.py
# @description test_fixture
# @author WcJun
# @date 2021/07/16
# ---------------------------------------------
import pytest


# ---------------------------------------------
# @pytest.fixture(scope='', params='', autouse='', ids='', name='')
# scope: function(default) | class | module | package/session
# params: parametrize -> [] | () | [{},{},...,{}] | ({},{},...,{})
# autouse: auto execution default: False
# ids: variable
# name: alisa
# ---------------------------------------------


# @pytest.fixture(scope='function', autouse=True)
# def hello_fixture():
#     """
#     hello_fixture
#     """
#     print('\nhello_fixture::do pre()')
#     yield
#     print('\nhello_fixture::do post()')

# ---------------------------------------------

# @pytest.fixture(scope='function', autouse=False, params=['Java', 'Python', 'C++'])
# def hello_fixture(request):
#     return request.param

# ---------------------------------------------

@pytest.fixture(
    scope='function',
    autouse=False,
    params=['Java', 'Python', 'Go'], ids=['J', 'P', 'G'],
    name='class_post_processor'
)
def hello_fixture(request):
    print('\nyield::hello_fixture::do pre()')
    yield request.param
    print('\nyield::hello_fixture::do post()')


class TestFixture:
    """
    test fixture
    """

    def test_do_not_fixture(self):
        """
        test_do_not_fixture
        """
        print('\ntest_do_not_fixture')

    def test_do_fixture(self, class_post_processor):
        """
        test_do_fixture
        """
        print('\ntest_do_fixture::' + str(class_post_processor))

    def test_do_auto_fixture(self):
        """
        test_do_auto_fixture
        """
        print('\ntest_do_auto_fixture')

    def test_do_global_fixture(self, global_class_post_processor):
        """
        test_do_auto_fixture
        """
        print('\ntest_do_global_fixture::' + str(global_class_post_processor))
