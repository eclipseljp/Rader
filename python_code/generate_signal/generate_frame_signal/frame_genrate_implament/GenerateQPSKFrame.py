"""
@author:caocongcong
"""
from generate_signal.generate_frame_signal.FrameGenerator import FrameGenerator
from primary_signal.const_value import constValue
import numpy as np


class GenerateQPSKFrame(FrameGenerator):
    def product_frame(self, fs, subcode_values, subconde_last_time):
        '''
        QPSK调制
        :param fs: 基础频率
        :param encode_values: 1, -1, j, -j 四种值，分别代表四种相位
        :param subconde_last_time: 一个编码持续时间
        :return: 调制完成后的信号
        '''
        sample_number = int(constValue.system_freq * subconde_last_time)
        time = np.linspace(0, sample_number, sample_number)
        frame_signal = np.zeros(sample_number * len(subcode_values))

        for i in len(subcode_values):
            if subcode_values[i] == '1':
                subcode_signal = np.cos(2 * np.pi * time / (constValue.system_freq / fs))
            elif subcode_values[i] == 'j':
                subcode_signal = np.cos(2 * np.pi * time / (constValue.system_freq / fs) + np.pi / 2)
            elif subcode_values[i] == '-1':
                subcode_signal = np.cos(2 * np.pi * time / (constValue.system_freq / fs) + np.pi)
            else:
                subcode_signal = np.cos(2 * np.pi * time / (constValue.system_freq / fs) + np.pi / 2 * 3)

            frame_signal[i * sample_number: (i + 1) * sample_number] = subcode_signal

        return frame_signal
