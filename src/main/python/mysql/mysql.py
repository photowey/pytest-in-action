# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file mysql
# @description mysql
# @author WcJun
# @date 2021/07/23
# ---------------------------------------------


import pymysql

from src.main.python.mysql.option import Options


class Mysql(object):

    def __init__(self, options: Options):
        self.options = options
        connection = self.connection()
        self.connection = connection

    def connection(self) -> pymysql.connect:
        connection: pymysql.connect = pymysql.connect(
            host=self.options.host, user=self.options.user,
            password=self.options.password, database=self.options.database, port=self.options.port)

        return connection

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

    def insert(self, sql: str, params: []):
        rows = 0
        cursor = self.connection.cursor()
        for params in params:
            single_rows = cursor.execute(sql, params)
            rows += single_rows
        cursor.close()
        self.commit()
        self.close()

        return rows
