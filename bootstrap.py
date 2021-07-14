# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file bootstrap
# @description bootstrap
# @author WcJun
# @date 2021/07/14
# ---------------------------------------------
import os

import pytest

python_path = 'src/main/python'

if __name__ == '__main__':
    # ---------------------------------------------
    # -s: 输出调试信息，包括打印信息
    # pytest.main(['-s'])
    # -v: 详细信息
    # pytest.main(['-v'])
    # ---------------------------------------------
    # 所有
    # pytest.main(['-vs'])
    # ---------------------------------------------
    # 指定用例
    # pytest.main(['-vs', './src/main/python/testinterface/test_interface.py'])
    # ---------------------------------------------
    # 指定文件夹
    # pytest.main(['-vs', './{}/testinterface'.format(python_path)])
    # ---------------------------------------------
    # -
    # ---------------------------------------------
    # 通过 nodeId 指定运行的用例
    # nodeId: 模块名-分隔符-类名-方法名-函数名 组成
    # ---------------------------------------------
    # 执行函数
    # pytest.main(['-vs', './{}/testinterface/test_interface.py::test_function'.format(python_path)])
    # ---------------------------------------------
    # 执行方法
    # pytest.main(['-vs', './{}/testinterface/test_interface.py::TestInterface::test_method'.format(python_path)])
    # ---------------------------------------------
    # -n: 线程数量
    # --reruns: 失败用例重试 (--reruns==2)
    # -x: 只要有一个用例报错,就停止
    # -k: 根据用例的部分名称--模糊匹配 $ pytest -vs [path] -k "hello"
    # @pytest.mark.run(order=2) 改变执行顺序
    # ---------------------------------------------
    # -
    # ---------------------------------------------
    # 采用 pytest.ini
    # 自定义-分组
    # $ pytest -m "smoke or user_manage"
    # ---------------------------------------------
    pytest.main()
    os.system('allure generate ./tmp -o ./report --clean')
