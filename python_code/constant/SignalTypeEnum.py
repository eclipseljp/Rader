"""
@author:caocongcong
"""
from enum import Enum, unique


@unique
class signal_type(Enum):
    single_fs = 1
    LFM = 2
