__author__ = 'cao'
from primary_signal.signal_source import signal_source
from primary_signal.get_primary_signal import priamry_signal
from util.Tool import show_Data
from primary_signal.ADC import AD
import scipy
from primary_signal.const_value import constValue

def signal_flow_show( primary_data):

    # 绘图进行观察，观察时域和频域
    show_Data(primary_data)
    # 进行滤波器测试
    ad_test = AD(primary_data, simutime, frame_time)
    # 观察变频
    after_con_down = ad_test.down_conversion("COS", 400, constValue.system_freq, primary_data)
    show_Data(after_con_down)
    after_fluter = ad_test.FIR_filter("400M", after_con_down)
    show_Data(after_fluter)
    # 使用FFT方法
    change_sample_rate = scipy.signal.resample(after_fluter, int(len(after_fluter)*constValue.first_sample_fs/constValue.system_freq))
    # # 使用滤波器方法
    # # change_sample_rate = scipy.signal.resample_poly(after_fluter, 6, 25)
    # show_Data(change_sample_rate)
    # # 进行滤波
    second_after_com_down = ad_test.down_conversion("COS", 60, constValue.first_sample_fs , change_sample_rate)
    # show_Data(second_after_com_down)
    # second_after_fluter = ad_test.FIR_filter("60M", second_after_com_down)


def all_flow_test(primary_data):
    # 进行完整的测试
    ad_test = AD(primary_data, simutime, frame_time)
    ad_test.AD_data()
    show_Data(ad_test.final_primary_data[1][2])



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
    # 进行全流程测试
    signal_flow_show(primary_data)