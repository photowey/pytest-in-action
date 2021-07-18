# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file test_api
# @description test_api
# @author WcJun
# @date 2021/07/14
# ---------------------------------------------


# ---------------------------------------------
# pytest 规范
# 1.模块名: 以 {@code test_} 开头 或者 以 {@code _test} 结尾
# 2.类型以 {@code Test} 开头
# 3.测试方法以: {@code test} 开头
# ---------------------------------------------
import allure
import pytest


@allure.feature('Feature1')
@allure.story('Story1')
@allure.testcase('http://my.tms.org/TESTCASE-1')
def test_foo():
    assert False


@allure.feature('Feature2')
@allure.story('Story2')
@allure.testcase('http://my.tms.org/TESTCASE-2')
def test_function():
    """
    test execution the function.
    """
    print('test execution function')


@allure.feature('测试模块::这儿是模块')
@allure.epic('define epic::epic 相当于总体描述')
class TestApi:
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

    @allure.story('test_allure_feature_story')
    @allure.title("test_allure_feature_title")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.issue("http://jira.lan/browse/ISSUE-9527")
    @allure.testcase("ttp://my.tms.org/browse/TESTCASE-9527")
    def test_allure_feature(self, logger):
        """
        test allure_feature \n
        Allure 中对严重级别的定义: \n
        1. Blocker 级别: 中断缺陷(客户端程序无响应，无法执行下一步操作)\n
        2. Critical 级别: 临界缺陷( 功能点缺失)\n
        3. Normal 级别: 普通缺陷(数值计算错误)\n
        4. Minor 级别: 次要缺陷(界面错误与UI需求不符)\n
        5. Trivial 级别: 轻微缺陷(必输项无提示，或者提示不规范)
        :return:
        """
        logger.info('do log::test_allure_feature!')
        print('test allure feature!')

    @allure.story('test_minor_minor')
    @allure.title("test_minor_minor")
    @pytest.mark.parametrize('country', ('CN', 'USA'))
    def test_minor(self, logger, country):
        """
        test_minor
        """
        logger.info('the country is {}'.format(country))
        assert country
