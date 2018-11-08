__author__ = 'cao'
from primary_signal.signal_source import signal_source
from primary_signal.get_primary_signal import priamry_signal
from util.Tool import show_Data, show_complex
from primary_signal.ADC import AD
import scipy
from primary_signal.const_value import constValue




def complex_ad_test(primary_data):
    ad_test = AD(primary_data, simutime, frame_time)
    ad_test.first_complex_conv(1,primary_data)
    show_complex(ad_test.first_complex_signal)

# 本文件对ADC进行测试
if __name__ == "__main__":
    # 首先获取原始信号
    signal = signal_source(0.4, 30, 1, [450], 2, [10, 0.4])
    signals = [signal]
    simutime = 500
    frame_time = 100
    priamry_signal_test = priamry_signal(signals, simutime)
    # 获取原始信号
    primary_data = priamry_signal_test.primary_data
    complex_ad_test(primary_data)