# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file bootstrap
# @description bootstrap
# @author WcJun
# @date 2021/07/14
# ---------------------------------------------
import pytest

python_path = 'src/main/python'

if __name__ == '__main__':
    # ---------------------------------------------
    # -s: 输出调试信息，包括打印信息
    # pytest.main(['-s'])
    # -v: 详细信息
    # pytest.main(['-v'])
    # ---------------------------------------------
    ## 所有
    # pytest.main(['-vs'])
    # ---------------------------------------------
    ## 指定用例
    ## pytest.main(['-vs', './src/main/python/testinterface/test_interface.py'])
    # ---------------------------------------------
    ## 指定文件夹
    pytest.main(['-vs', './{}/testinterface'.format(python_path)])
