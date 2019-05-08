"""
@author:caocongcong
"""
from generate_signal.constant.genrate_setting_constant import generate_setting_constant
from generate_signal.genrate_pri.PriGenerator import PriGenerator
from generate_signal.genrate_pri.pri_generate_implament.PriGeneratorUtil import get_start_time
import random


class GenerateJitterPri(PriGenerator):
    '''
    进行重频捷变的生成
    '''

    def get_next_pri(self, pri_value, jitter_value, jitter_number):
        '''
        根据捷变参数生成下一个间隔时间
        :param pri_value:  原始的间隔时间
        :param jitter_value: 捷变的范围
        :param jitter_number:  捷变的个数
        :return: 返回下一个间隔时间
        '''
        if jitter_number <= 0:
            return random.randrange(pri_value - jitter_value, pri_value + jitter_value, 1)
        else:
            return random.randrange(pri_value - jitter_value, pri_value + jitter_value,
                                    round((jitter_value * 2 + 0.0) / jitter_number,
                                          generate_setting_constant.pri_accuracy))

    def product_pri(self, simu_time, pw, pri_value, jitter_vaule, jitter_number, begin_time):
        '''
        进行PRI捷变的生成
        :param simu_time: 仿真总时间
        :param pw: 脉宽
        :param pri_value: 原始的PRI值
        :param jitter_vaule: pri的变化值
        :param jitter_number: 捷变点的个数
        :return:
        '''
        pri_data = []

        # 生成重频的过程
        if begin_time == 0:
            start_time = get_start_time(pri_value)
        else:
            start_time = begin_time
        # 保留两位
        # print("当前生成的起始时间", start_time)
        current_time = start_time
        # 开始生成信号
        # 当当前的时间不超过仿真的总时间
        while current_time < simu_time:
            # 生成一个脉冲
            pri_data.append(current_time)
            current_time += (pw + self.get_next_pri(pri_value, jitter_vaule))
        return pri_data
