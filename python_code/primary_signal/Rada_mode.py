__author__ = 'caocongcong'
from enum import Enum

# 使用枚举类来定义频率类型
class FS_type(Enum):
    # 固定频率为1
    fs_fixed = 1
    # 频率捷变为2
    fs_agile = 2
    # 频率分集为3
    fs_diversity = 3
    # 脉间变频为4
    fs_pluse_group_conversion = 4
    # LFM信号
    LFM = 5
    # 大带宽的LFM信号
    lager_bandwidth_LFM = 6


# 使用枚举类型来定义重频类型
class PRI_type(Enum):
    # 固定重频为1
    pri_fixed = 1
    # 重频参差/抖动
    pri_irre = 2
    # 脉组雷达
    pri_plus_group_conversion = 3


if __name__ == "__main__":
    print(FS_type.fs_fixed == (FS_type(1)))