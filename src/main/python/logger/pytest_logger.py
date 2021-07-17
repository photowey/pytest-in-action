# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file test_logger
# @description test_logger
# @author WcJun
# @date 2021/07/16
# ---------------------------------------------

import logging
import os
import time
from datetime import datetime


def makedir_if_necessary(target_path):
    """
    makedir if necessary
    :param target_path:
    :return:
    """
    if not os.path.exists(target_path):
        os.makedirs(target_path)


class PytestLogger:
    """
    日志记录控件类
    """

    def __init__(self):
        """
        设置 logger 日志 path
        """
        root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        logger_path = os.path.join(root_path + os.sep + 'log')

        makedir_if_necessary(logger_path)

        self.log_name = logger_path + os.sep + time.strftime('%Y%m%d%H%M%S') + '.log'
        self.strf_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 创建一个 logger
        pylogger = logging.getLogger('pylogger')
        pylogger.setLevel(logging.DEBUG)
        self.logger = pylogger

    def print_console(self, level, message):
        """
        打印日志，支持写入日志和输入到控制台
        """

        # 创建一个 handler，用于写入日志文件
        file_handler = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        # 再创建一个 handler，用于输出到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)

        # 定义 handler 的输出格式
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(filename)s[line:%(lineno)d] - %(levelname)s : %(message)s')

        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # 给 logger 添加 handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

        # 记录一条日志
        self.switch(level, message)

        self.logger.removeHandler(stream_handler)
        self.logger.removeHandler(file_handler)

    def debug(self, message):
        """打印debug日志"""
        self.print_console(logging.DEBUG, message)

    def info(self, message):
        """打印普通信息"""
        self.print_console(logging.INFO, message)

    def warning(self, message):
        """打印警告"""
        self.print_console(logging.WARNING, message)

    def error(self, message):
        """打印错误"""
        self.print_console(logging.ERROR, message)

    def switch(self, level, message):
        """
        定义 switch() 来实现 switch 语法
        """
        handler_map = {
            logging.DEBUG: self.logger.debug,
            logging.INFO: self.logger.info,
            logging.WARNING: self.logger.warning,
            logging.ERROR: self.logger.error
        }
        handler = handler_map.get(level)
        if handler:
            handler(message)
