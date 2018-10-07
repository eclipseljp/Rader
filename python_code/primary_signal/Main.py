__author__ = 'caocongcong'
from primary_signal.signal_source import signal_source
import numpy as np
import matplotlib.pyplot as plt
from primary_signal.get_primary_signal import priamry_signal
def Main():
    # 首先获取需要产生的信号
    signals = get_signals()
    # 设定仿真时间
    simutime = 5000
    # 进行模拟信号的产生
    priamry_signal_test = priamry_signal(signals, simutime)
    # 写入原始数据
    priamry_signal_test.write_data("..\data\primary_data.txt")
    priamry_signal_test.show_data(1000, 2000)


def get_signals():
    '''
    使用该函数产生需要的信号,各类信号的产生方式可以参见
    :return:返回信号组成的list
    '''
    # 固定频率和抖动重频
    # test_signal = signal_source(0.4, 30, 1,  [50], 2, [100, 0.4])
    # 固定频率和脉组重频
    #test_signal = signal_source(0.4, 30, 1,  [50], 3, [100, 10, 0.4])
    # 频率抖动和抖动重频
    # test_signal = signal_source(0.4, 30, 2,  [50, 10], 2, [100, 0.4])
    # 频率抖动和脉组重频
    # test_signal = signal_source(0.4, 30, 2,  [50, 10], 3, [100, 10, 0.4])
    # 频率分集和抖动重频
    # test_signal = signal_source(0.4, 30, 3,  [50, 55, 60, 65, 70], 2, [100, 0.4])
    #  频率分集和脉组重频
    # test_signal = signal_source(0.4, 30, 3,  [50, 55, 60, 65, 70], 3, [100, 10, 0.4])
    # 频率脉组捷变和抖动重频
    # test_signal = signal_source(0.4, 30, 4,  [50, 8, 0.2], 2, [100, 0.4])
    # 频率脉组捷变和脉组重频
    # test_signal = signal_source(0.4, 30, 4,  [50, 8, 0.2], 3, [100, 10, 0.4])
    # 频率捷变的LFM
    # test_signal = signal_source(1, 30, 5,  [50, 40, 0.2], 1, [100])
    # 跨帧的大带宽LFM
    # test_signal = signal_source(1, 30, 6,  [50, 40, 0.2, 4], 1, [100])

    # 正式测试
    # 首先生成一组信号
    test_signal_1 = signal_source(0.4, 30, 1,  [50], 2, [100, 0.4])
    test_signal_2 = signal_source(0.4, 30, 2,  [50, 10], 3, [100, 10, 0.4])
    test_signal_3 = test_signal = signal_source(0.4, 30, 4,  [50, 8, 0.2], 2, [100, 0.4])
    # 将一组信号合并成一个list
    test_signal = [test_signal_1, test_signal_2, test_signal_3]
    return test_signal



if __name__ == "__main__":
    Main()
