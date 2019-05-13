"""
@author:caocongcong
"""
from generate_signal.generate_frame_signal.FrameGenerator import FrameGenerator
from primary_signal.const_value import constValue
import numpy as np


class GenerateBPSKFrame(FrameGenerator):

    def product_frame(self, fs, subcode_values, subconde_last_time):
        '''
        进行BPSK调制
        如果是0： cos(2*pi*wt)
        如果是1： -cos(2*pi*wt)
        :param fs: 帧的基准频率
        :param subcode_values: 子码数组
        :param subconde_last_time: 子码持续时间
        :return: 生成的单帧信号
        '''
        sample_number = int(constValue.system_freq * subconde_last_time)
        time = np.linspace(0, sample_number, sample_number)
        frame_signal = np.zeros(sample_number * len(subcode_values))
        subcode_signal =  np.cos(2 * np.pi * time / (constValue.system_freq / fs))
        for i in len(subcode_values):
            if subcode_values[i] == 0:
                frame_signal[i*sample_number : (i+1)*sample_number] = subcode_signal
            else:
                frame_signal[i * sample_number: (i + 1) * sample_number] = -subcode_signal

        return frame_signal


