"""
@author:caocongcong
"""
from enum import Enum


class frame_type_enum(Enum):
    '''
    枚举帧的种类
    '''
    # 固定频率为1
    single_fs = 1

    # 线性调频为
    lfm = 2