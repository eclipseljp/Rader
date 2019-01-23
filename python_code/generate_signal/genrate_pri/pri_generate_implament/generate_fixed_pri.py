"""
@author:caocongcong
"""
from generate_signal.genrate_pri.pri_generate_implament.pri_param_method import pri_param_method

class generate_fixed_method(pri_param_method):
    '''
    进行固定重频的生成
    '''
    def __init__(self):
        # 最终生成的重频数据
        self.pri_data = []

    def generate_pri(self, simutime, pw, params):
        # 生成重频的过程
        signal_pri = params[0]
        start_time = self.get_start_time(signal_pri)
        # 保留两位
        # print("当前生成的起始时间", start_time)
        current_time = start_time
        # 开始生成信号
        # 当当前的时间不超过仿真的总时间
        while current_time < simutime:
            # 生成一个脉冲
            self.pri_data.append(current_time)
            current_time += (pw + signal_pri)

    def get_pri_data(self):
        return self.pri_data