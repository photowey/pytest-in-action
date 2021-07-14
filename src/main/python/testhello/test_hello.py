# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file test_hello
# @description test_hello
# @author WcJun
# @date 2021/07/14
# ---------------------------------------------


# ---------------------------------------------
# pytest 规范
# 1.模块名: 以 {@code test_} 开头 或者 以 {@code _test} 结尾
# 2.类型以 {@code Test} 开头
# 3.测试方法以: {@code test} 开头
# ---------------------------------------------


class TestSayHello:
    """
    test say hello
    """

    def test_say_hello(self):
        """
        say hello
        :return:
        """
        print('hello world!')
        return 'say Hello from pytest-in-action service!'
