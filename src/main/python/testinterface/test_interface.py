# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file test_interface
# @description test_interface
# @author WcJun
# @date 2021/07/14
# ---------------------------------------------


# ---------------------------------------------
# pytest 规范
# 1.模块名: 以 {@code test_} 开头 或者 以 {@code _test} 结尾
# 2.类型以 {@code Test} 开头
# 3.测试方法以: {@code test} 开头
# ---------------------------------------------
import pytest


def test_function():
    """
    test execution the function.
    """
    print('test execution function')


class TestInterface:
    """
    test interface
    """

    age = 18

    @pytest.mark.run(order=3)
    def test_interface(self):
        """
        test interface
        :return:
        """
        print('test interface!')

    @pytest.mark.run(order=2)
    def test_method(self):
        """
        test method
        :return:
        """
        print('test method!')

    @pytest.mark.run(order=1)
    def test_ordering(self):
        """
        test ordering
        :return:
        """
        print('test method!')

    @pytest.mark.smoke
    def test_module_smoke(self):
        """
        test module.smoke test
        :return:
        """
        print('test module.smoke!')

    @pytest.mark.user_manage
    def test_module_user_manage(self):
        """
        test module.user_manage test
        :return:
        """
        print('test module.user!')

    @pytest.mark.skip(reason='have to skip...')
    def test_skip(self):
        """
        test skip
        :return:
        """
        print('test skip!')

    @pytest.mark.skipif(age > 16, reason='have to skip if...')
    def test_skip_if(self):
        """
        test skip_if
        :return:
        """
        print('test skip if!')
