"""
@author:caocongcong
"""
from generate_signal.genrate_pri.PriGenerator import PriGenerator
from generate_signal.genrate_pri.pri_generate_implament.PriGeneratorUtil import get_start_time


class GenerateFixedPri(PriGenerator):
    '''
    进行固定重频的生成
    '''

    def product_pri(self, simu_time, pw, signal_pri):
        '''
        固定重频生成的实现函数
        :param simu_time: 整个系统仿真时间
        :param pw: 脉宽
        :param signal_pri: 重频的值
        :return: 返回生成的重频
        '''
        pri_data = []

        # 生成重频的过程
        start_time = get_start_time(signal_pri)
        # 保留两位
        # print("当前生成的起始时间", start_time)
        current_time = start_time
        # 开始生成信号
        # 当当前的时间不超过仿真的总时间
        while current_time < simu_time:
            # 生成一个脉冲
            pri_data.append(current_time)
            current_time += (pw + signal_pri)
        return pri_data
