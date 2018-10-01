__author__ = 'caocongcong'
import numpy as np
from primary_signal.const_value import constValue
import matplotlib.pyplot as plt
# 脉冲类，记录一个脉冲
class pluse:
    # 初始化函数
    def __init__(self, fs, begin_time, pw, doa):
        '''
        :param fs: 该帧的主频,单位为Mhz
        :param begin_time: 该帧的起始时间
        :param pw: 该帧的持续时间
        :param doa: 到达角
        :return:
        '''
        self.fs = fs
        self.begin_time = begin_time
        self.pw = pw
        self.doa = doa

    def get_analog_signal(self):
        '''
        生成模拟信号
        :return: 产生的numpy数组
        '''
        # 生成的信号的点数
        sample_number = int(constValue.system_freq * self.pw)
        self.t = np.linspace(0, sample_number, sample_number)
        #print(self.t)
        #print(constValue.system_freq/self.fs)
        self.plus_signal = (1+np.sin(2*np.pi*self.t/(constValue.system_freq/self.fs)))/2

    # 绘制波形信息
    def draw_data(self):
        plt.plot(self.t, self.plus_signal)
        plt.show()



if __name__ == "__main__":
    pluse_test = pluse(20, 0, 100, 30)
    pluse_test.get_analog_signal()
    pluse_test.draw_data()
