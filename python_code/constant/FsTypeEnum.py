"""
@author:caocongcong
"""
from enum import Enum, unique

@unique
class fs_type(Enum):
    fs_fixed = "频率固定"
    fs_group = "频率分集"
    fs_jitter_intra_pulse = "频率脉内捷变"
    fs_jitter_between_pulse = "频率脉间捷变"
    fs_big_band_lfm = "大带宽LFM"
    fs_jitter_lfm = "频率捷变LFM"