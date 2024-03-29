"""
@author:caocongcong
"""
from generate_signal.generate_frame_signal.frame_genrate_implament.generate_frame_method import generate_frame_method
from primary_signal.const_value import constValue
import numpy as np


class genrate_lfm_signal(generate_frame_method):
    def __init__(self):
        self.frame_data = None

    def generate_frame_data(self, param, pw):
        '''
        :param  param[0]=begin_fs:起始频率
        :param param[1] = band : 带宽
        :param pw: 信号的脉宽
        计算公式是: sin(2*pi*f0*t + pi*k*t*t)
        '''
        begin_fs = param[0]
        Band = param[1]
        # 采样的点数
        N = pw * constValue.system_freq
        # 采样时间
        k = Band / pw
        t = np.linspace(0, pw, N)
        # signal = 0.5*np.sin(2*np.pi*begin_fs*t + np.pi*k*t*t)+0.5
        self.frame_data = np.sin(2 * np.pi * begin_fs * t + np.pi * k * t * t)

    def get_priamary_data(self):
        return self.frame_data
