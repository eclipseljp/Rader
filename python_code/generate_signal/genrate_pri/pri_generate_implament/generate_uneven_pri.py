"""
@author:caocongcong
"""
from generate_signal.genrate_pri.pri_generate_implament.pri_param_method import pri_param_method


class generate_uneven_pri(pri_param_method):

    def __init__(self):
        self.pri_data = []

    def generate_pri(self, simutime, pw, param):
        # 获取得到的PRI参数
        signal_pris = param[0]
        # 首先生成一段不超过PRI的随机时间作为起始时间
        start_time = self.get_start_time(signal_pris[0])
        # 当前时间就是起始时间
        current_time = start_time
        # pri的计数器
        pri_order = 0
        pri_num = len(signal_pris)
        while current_time < simutime:
            if (pri_order < pri_num):
                # 使用当前的重频不变
                current_time = round(current_time, 2)
                self.pri_data.append(current_time)
                current_time += (pw + signal_pris[pri_order])
                pri_order += 1
            else:
                # pri的计数器清零
                pri_order = 0

    def get_pri_data(self):
        return self.pri_data
