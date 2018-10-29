__author__ = 'cao'
from primary_signal.signal_source import signal_source
from primary_signal.get_primary_signal import priamry_signal
import matplotlib.pyplot as plt
import numpy as np
from primary_signal.Tool import show_Data
from primary_signal.ADC import AD

def show(data):
    pass
# 本文件对ADC进行测试
if __name__ == "__main__":
    # 首先获取原始信号
    signal = signal_source(0.4, 30, 1, [550], 2, [10, 0.4])
    signals = [signal]
    simutime = 500
    frame_time = 100
    priamry_signal_test = priamry_signal(signals, simutime)
    # 获取原始信号
    primary_data = priamry_signal_test.primary_data
    # 绘图进行观察，观察时域和频域
    show_Data(primary_data[0:12000])
    # 进行滤波器测试
    ad_test = AD(primary_data, simutime, frame_time)
    # 滤波器效果不错
    # after_fluter = ad_test.FIR_filter("60M", primary_data)
    # show_Data(after_fluter)
    # 观察变频
    after_con_down = ad_test.down_conversion("COS", 400, 1200, primary_data)
    show_Data(after_con_down)
    after_fluter = ad_test.FIR_filter("400M", after_con_down)
    show_Data(after_fluter)
