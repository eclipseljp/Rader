__author__ = 'cao'
import scipy.signal as signal
import numpy as np
import pylab as plt
from primary_signal.const_value import constValue
#进行滤波器设计
def fluter_design(n, base_band, pass_band, system_fs):
    '''
    进行滤波器设计,默认的低通滤波器设计
    :param n: 滤波器的阶数n
    :param base_band: 基带的频率
    :param pass_band: 过渡带的频率
    :param system_fs: 系统频率
    :return:返回滤波器的抽头
    '''
    # 宽带参数
    band_param =(0, base_band/system_fs, (base_band+pass_band)/system_fs, 0.5)
    # print(system_fs)
    # print(band_param)
    gain_param = [1, 0.001]
    b = signal.remez(n,band_param, gain_param)
    return b


# 进行参数选择
def choose_param(base_band, pass_band, system_fs, len_param):
    fig = plt.figure()
    for length in len_param:
        try:
            b = fluter_design(length, base_band, pass_band, system_fs)
            w, h = signal.freqz(b, 1)
            plt.plot(w / 2 / np.pi, 20 * np.log10(np.abs(h)), label=str(length))
        except:
            print("当前的length",str(length), "不能收敛")


    plt.legend()
    plt.xlabel(u"f/fs")
    plt.ylabel(u"amplitude(dB)")
    plt.title(u"remez design fluter")
    plt.show()

if __name__ == "__main__":
    # base_length = 30
    # add_length = 10
    # len_param = []
    # for i in range(5):
    #     len_param.append(base_length)
    #     base_length += add_length
    # choose_param(constValue.first_fluter_base, constValue.first_fluter_pass, constValue.system_freq, len_param)
    base_length = 10
    add_length = 10
    len_param = []
    for i in range(5):
        len_param.append(base_length)
        base_length += add_length
    choose_param(constValue.first_fluter_base, constValue.first_fluter_pass, constValue.system_freq, len_param)



