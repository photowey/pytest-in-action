# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file test_lifecycle.py
# @description test_lifecycle
# @author WcJun
# @date 2021/07/15
# ---------------------------------------------


class TestLifecycle:
    """
    test lifecycle
    """

    def setup_class(self):
        """
        setup_class
        """
        print('execution setup_class()!')

    def setup(self):
        """
        setup
        """
        print('execution setup()!')

    def teardown(self):
        """
        teardown
        """
        print('execution teardown()!')

    def teardown_class(self):
        """
        teardown_class
        """
        print('execution teardown_class()!')
