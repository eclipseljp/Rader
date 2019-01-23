"""
@author:caocongcong
"""
from enum import Enum


class signal_type_enum(Enum):
    '''
    枚举的种类
    '''
    # 固定重频为1
    pri_fixed = 1

    # 重频抖动
    pri_irre = 2

    # 重频参差
    pri_uneven = 3

    # 脉组雷达
    pri_group_conversion = 4