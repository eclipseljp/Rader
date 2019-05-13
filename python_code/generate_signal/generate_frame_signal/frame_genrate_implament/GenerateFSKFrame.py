"""
@author:caocongcong
"""
from generate_signal.generate_frame_signal.FrameGenerator import FrameGenerator
from primary_signal.const_value import constValue
import numpy as np


class GenerateFSKFrame(FrameGenerator):

    def product_frame(self, base_fs, fs_values, sub_time):
        '''
        进行FSK的调制
        :param base_fs:基础频率
        :param fs_values:  调制频率
        :param sub_time: 子带的时长
        :return: 调制成功的信号
        '''
        sample_number = int(constValue.system_freq * sub_time)
        time = np.linspace(0, sample_number, sample_number)
        frame_signal = np.zeros(sample_number * len(fs_values))

        for i in len(fs_values):
            subcode_signal = np.cos(2 * np.pi * time / (constValue.system_freq / fs_values[i]))
            frame_signal[i * sample_number: (i + 1) * sample_number] = subcode_signal

        return frame_signal
