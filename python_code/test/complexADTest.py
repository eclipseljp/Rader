__author__ = 'cao'
import numpy as np
from util.Tool import show_Data
# 进行复数的AD采样测试
def signal_generate(sample_freq, band, Intermediate_freq, pw, SNR, simu_time):
    t = np.linspace(0, int(sample_freq*pw), int(sample_freq*pw))
    # primary_signal = np.cos(np.pi * band / pw * (t/ sample_freq)*(t/sample_freq))*np.cos(2 * np.pi * Intermediate_freq * t / sample_freq) \
    #         - np.sin(np.pi * band / pw * (t / sample_freq)*(t/sample_freq))*np.sin(2 * np.pi * Intermediate_freq * t / sample_freq)
    primary_signal = np.cos(np.pi * band * (t / sample_freq) * (t / sample_freq)) * np.cos(
        2 * np.pi * Intermediate_freq * t / sample_freq) \
                     - np.sin(np.pi * band  * (t / sample_freq) * (t / sample_freq)) * np.sin(
        2 * np.pi * Intermediate_freq * t / sample_freq)


    # 将雷达信号移动到一半的地方去
    result = np.zeros(int(simu_time * sample_freq ))
    result [int(simu_time * sample_freq/2) :  int(simu_time *sample_freq/2)+len(primary_signal)] += primary_signal
    # 将SNR由dB单位转化成倍数关系
    snr = 10 ** (SNR / 10.0)
    # 计算原始信号功率
    xpower = np.sum(primary_signal ** 2) / len(result)
    # 根据信噪比计算已经增加的噪声的功率
    npower = xpower / snr
    # 随机生成噪声
    noise = np.random.randn(len(result)) * np.sqrt(npower)
    # 将噪声叠加到原始信号上去
    result += noise
    return result

def complexMix(sample_freq, Intermediate_freq, priamry_signal):
    t = np.linspace(0, int(sample_freq * simu_time), int(sample_freq * simu_time))
    complexMix_base = np.exp(-1j*2*np.pi*Intermediate_freq/sample_freq)
    after_mix = primary_signal*complexMix_base
    return after_mix

if __name__ == "__main__":
    sample_freq = 480e6
    band = 30e6
    Intermediate_freq = 300e6
    SNR = 20
    # 30微秒
    pw = 150e-6
    # 观测时间
    simu_time = 1e-3
    primary_signal = signal_generate(sample_freq, band, Intermediate_freq, pw, SNR, simu_time)
    show_Data(primary_signal)
    mixSignal = complexMix(sample_freq, Intermediate_freq, primary_signal)
    show_Data(mixSignal)


