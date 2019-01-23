"""
@author:caocongcong
"""
import random

from generate_signal.genrate_pri.pri_generate_implament.pri_param_method import pri_param_method
from generate_signal.constant.genrate_setting_constant import generate_setting_constant


class generate_irre_pri(pri_param_method):

    def __init__(self):
        self.pri_data = []

    def generate_pri(self, simutime, pw, params):
        signal_pri = params[0]
        signal_pri_range = params[1]

        # 首先生成一段不超过PRI的随机时间作为起始时间
        start_time = self.get_start_time(signal_pri)
        # 保留两位
        current_time = start_time
        while current_time < simutime:
            self.pri_data.append(current_time)
            # 随机生成与下一个脉冲的间隔时间
            tmp_prt = signal_pri * (1 + random.random() * signal_pri_range - (signal_pri_range / 2))
            # 累加
            current_time += (pw + tmp_prt)
            # 控制精度
            current_time = round(current_time,  generate_setting_constant.pri_accuracy)

    def get_pri_data(self):
        return self.pri_data
