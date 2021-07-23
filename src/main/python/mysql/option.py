# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file mysql_options
# @description mysql_options
# @author WcJun
# @date 2021/07/23
# ---------------------------------------------


class Options(object):
    def __init__(self, host: str, user: str, password: str, database: str, port: int):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
