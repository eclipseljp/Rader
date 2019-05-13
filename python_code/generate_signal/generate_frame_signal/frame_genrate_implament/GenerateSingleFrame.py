"""
@author:caocongcong
"""
from generate_signal.generate_frame_signal.FrameGenerator import FrameGenerator
from primary_signal.const_value import constValue
import numpy as np


class GenerateSingleFrame(FrameGenerator):

    def product_frame(self, fs, pw):
        '''
        进行单频点信号的生成
        :param fs: 频率
        :param pw: 脉宽
        :return:生成的信号
        '''
        sample_number = int(constValue.system_freq * pw)
        time = np.linspace(0, sample_number, sample_number)
        frame_signal = np.sin(2 * np.pi * time / (constValue.system_freq / fs))
        return frame_signal
