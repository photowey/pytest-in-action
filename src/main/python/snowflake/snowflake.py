# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file snowflake
# @description snowflake
# @author WcJun
# @date 2021/07/19
# ---------------------------------------------
# Twitter's Snowflake algorithm implementation which is used to generate distributed IDs.
# https://github.com/twitter-archive/snowflake/blob/snowflake-2010/src/main/scala/com/twitter/service/snowflake/IdWorker.scala
# copy from: https://www.cnblogs.com/oklizz/p/11865750.html
# ---------------------------------------------


import time

from src.main.python.snowflake.exceptions import InvalidSystemClock

WORKER_ID_BITS = 5
data_center_id_BITS = 5
SEQUENCE_BITS = 12

MAX_WORKER_ID = -1 ^ (-1 << WORKER_ID_BITS)
MAX_data_center_id = -1 ^ (-1 << data_center_id_BITS)

WORKER_ID_SHIFT = SEQUENCE_BITS
data_center_id_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS
TIMESTAMP_LEFT_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS + data_center_id_BITS

SEQUENCE_MASK = -1 ^ (-1 << SEQUENCE_BITS)

TWEPOCH = 1288834974657


class SnowflakeIdWorker(object):
    """
    Id 生成器
    """

    def __init__(self, data_center_id, worker_id, sequence=0):
        """
        初始化
        :param data_center_id: 数据中心(机器区域)ID
        :param worker_id: 机器ID
        :param sequence: 其实序号
        """
        # sanity check
        if worker_id > MAX_WORKER_ID or worker_id < 0:
            raise ValueError('worker_id值越界')

        if data_center_id > MAX_data_center_id or data_center_id < 0:
            raise ValueError('data_center_id值越界')

        self.worker_id = worker_id
        self.data_center_id = data_center_id
        self.sequence = sequence

        self.last_timestamp = -1  # 上次计算的时间戳

    def _gen_timestamp(self):
        """
        生成整数时间戳
        :return:int timestamp
        """
        return int(time.time() * 1000)

    def next_id(self):
        """
        生成新的Id
        :return:
        """
        timestamp = self._gen_timestamp()

        # 时钟回拨
        if timestamp < self.last_timestamp:
            raise InvalidSystemClock

        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & SEQUENCE_MASK
            if self.sequence == 0:
                timestamp = self._til_next_millis(self.last_timestamp)
        else:
            self.sequence = 0

        self.last_timestamp = timestamp

        new_id = ((timestamp - TWEPOCH) << TIMESTAMP_LEFT_SHIFT) | \
                 (self.data_center_id << data_center_id_SHIFT) | \
                 (self.worker_id << WORKER_ID_SHIFT) | self.sequence
        return new_id

    def _til_next_millis(self, last_timestamp):
        """
        等到下一毫秒
        """
        timestamp = self._gen_timestamp()
        while timestamp <= last_timestamp:
            timestamp = self._gen_timestamp()
        return timestamp
