# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file test_hello
# @description test_hello
# @author WcJun
# @date 2021/07/14
# ---------------------------------------------
import pytest


# ---------------------------------------------
# pytest 规范
## 1.模块名: 以 {@code test_} 开头 或者 以 {@code _test} 结尾
## 2.类型以 {@code Test} 开头
## 3.测试方法以: {@code test_} 开头
# ---------------------------------------------


class TestWeb:
    """
    test web
    """

    def test_web(self):
        """
        test web
        :return:
        """
        print('test web!')

