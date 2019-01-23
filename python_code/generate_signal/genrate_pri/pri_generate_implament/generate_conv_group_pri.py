"""
@author:caocongcong
"""
import random

from generate_signal.genrate_pri.pri_generate_implament.pri_param_method import pri_param_method


class generate_conv_group_pri(pri_param_method):

    def __init__(self):
        self.pri_data = []

    def generate_pri(self, simutime, pw, param):
        signal_pri = param[0]
        # 获取重频的脉组个数
        pri_num = param[1]
        # 重频的变化范围
        signal_pri_range = param[2]
        # 首先生成一段不超过PRI的随机时间作为起始时间
        start_time = self.get_start_time(signal_pri)
        # 当前时间就是起始时间
        current_time = start_time
        # pri的计数器
        pri_order = 0
        tmp_prt = signal_pri * (1 + random.random() * signal_pri_range - (signal_pri_range / 2))
        while current_time < simutime:
            if (pri_order < pri_num):
                # 使用当前的重频不变
                current_time = round(current_time, 2)
                pri_order += 1
                self.pri_data.append(current_time)
                current_time += pw + tmp_prt
            else:
                # 生成新的重频
                tmp_prt = signal_pri * (1 + random.random() * signal_pri_range - (signal_pri_range / 2))
                # pri的计数器清零
                pri_order = 0

    def get_pri_data(self):
        return self.pri_data
