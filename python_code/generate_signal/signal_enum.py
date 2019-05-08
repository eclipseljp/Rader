"""
@author:caocongcong
"""
from enum import Enum


class InterModulationEnum(Enum):
    '''脉内调制的类型'''

    point_freq_modulation = 1  # 点频

    liner_freq_modulation = 2  # 线性调频

    no_liner_freq_modulation = 3  # 非线性调频

    bpsk = 4  # 二相编码信号

    qpsk = 5  # 四相编码信号

    fsk = 6  # 频移键控信号


class RepetitionRateEnum(Enum):
    """雷达重频的类型"""
    pri_fixed = 1  # 固定重频
    pri_irregular = 2  # 重频参差
    pri_jitter = 3  # 重频抖动
    pri_group_irregular = 4  # 脉组参差


class FrequencyEnum(Enum):
    """频率类型设置"""
    fs_fixed = 1  # 固定频率
    fs_jitter = 2  # 频率捷变
    fs_diversity = 3  # 频率分集
    fs_group_jitter = 4  # 脉组变频
