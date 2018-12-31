"""
@author:caocongcong
"""
from enum import Enum, unique

@unique
class pri_type(Enum):
    pri_group = "重频脉组"
    pri_fixed = "重频固定"
    pri_deviation = "重频参差"
    pri_jitter = "重频抖动"



