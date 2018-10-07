__author__ = 'caocongcong'
# 原始信号类，进行原始信号的生成
from primary_signal.const_value import constValue
import numpy as np
import matplotlib.pyplot as plt
class priamry_signal:
    def __init__(self, signals, simutime):
        '''
        该类为原始信号的生成类
        :param signals: 为仿真环境中信号源类组成的list
        :param simutime: 仿真的时间
        :return:
        '''
        self.signals = signals
        self.simutime = simutime

    def merge_signal(self):
        # 进行多个信号源和合并
        # 首先生成信号0的数据
        self.signals[0].get_plus(self.simu_time)
        self.signals[0].get_analog_signal()
        self.signals[0].add_channel()
        self.primary_data = self.signals[0].signal
        # 将其他信号全部叠加上去
        for i in range(1, len(self.signals)):
            self.signals[i].get_plus(self.simu_time)
            self.signals[i].get_analog_signal()
            self.signals[i].add_channel()
            self.primary_data += self.signals[i].signal

    def write_data(self, file_path):
        '''
        将信号的原始数据进行写入
        :param file_path: 文件路径
        :return:
        '''
        print("开始写入")
        np.savetxt(file_path, self.primary_data)
        print("写入完毕")

    def write_param(self, file_path):
        '''
        将型号的类型进行写入
        :param file_path: 需要写入的文件路径
        :return:
        '''

    def show_data(self, begin_time, end_time):
        '''
        给定首尾时间绘制一部分图像
        :param begin_time:起始时间
        :param end_time: 结束时间
        :return:
        '''
        # 起始的点
        begin_number = begin_time * constValue.system_freq
        # 结束的点
        end_number = end_time * constValue.system_freq
        # 进行绘制
        plt.plot(self.primary_data[begin_number:end_number])
        plt.show()
