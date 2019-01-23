"""
@author:caocongcong
"""
import random
from generate_signal.constant.genrate_setting_constant import generate_setting_constant


class pri_param_method():
    def generate_pri(self, simutime, pw, param):
        pass

    def get_pri_data(self):
        pass

    def get_start_time(self, signal_pri):
        # 随机生成一个小于重频的时间做为起始时间
        start_time = random.random() * signal_pri
        # 保留两位小数
        start_time = round(start_time, generate_setting_constant.pri_accuracy)
        return start_time