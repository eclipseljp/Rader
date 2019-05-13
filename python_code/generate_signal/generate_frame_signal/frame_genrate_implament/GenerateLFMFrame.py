"""
@author:caocongcong
"""
from generate_signal.generate_frame_signal.FrameGenerator import FrameGenerator
from generate_signal.generate_frame_signal.frame_genrate_implament.generate_frame_method import generate_frame_method
from primary_signal.const_value import constValue
import numpy as np


class GenerateLFMFrame(FrameGenerator):

    def product_frame(self, begin_fs, band, pw):
        '''
        :param  begin_fs:起始频率
        :param band : 带宽
        :param pw: 信号的脉宽
        计算公式是: sin(2*pi*f0*t + pi*k*t*t)
        '''
        # 采样的点数
        N = pw * constValue.system_freq
        # 采样时间
        k = band / pw
        t = np.linspace(0, pw, N)
        # signal = 0.5*np.sin(2*np.pi*begin_fs*t + np.pi*k*t*t)+0.5
        frame_data = np.sin(2 * np.pi * begin_fs * t + np.pi * k * t * t)
        return frame_data

