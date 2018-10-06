__author__ = 'caocongcong'
from primary_signal.signal_source import signal_source
import numpy as np
import matplotlib.pyplot as plt
def Main():
    # 生成一个测试信号
    # test_single_signal()
    # 测试多组信号
    #test_mul_signal()
    # 测试线性调频
    test_LFM_singal()


def test_single_signal():
    # 生成一个测试信号
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
    test_signal = signal_source(0.4, 30, 4,  [50, 8, 0.2], 2, [100, 0.4])
    # 频率脉组捷变和脉组重频
    # test_signal = signal_source(0.4, 30, 4,  [50, 8, 0.2], 3, [100, 10, 0.4])
    simu_time = 5000

    # 生成PDW真值
    test_signal.get_plus(simu_time)
    # 生成模拟信号
    test_signal.get_analog_signal()
    # 增加环境噪声
    test_signal.add_channel()
    test_signal.draw(100000, 1200000)
    print("开始写入")
    np.savetxt("..\data\one.txt", test_signal.signal)

def test_mul_signal():
    # 首先生成一组信号
    test_signal_1 = signal_source(0.4, 30, 1,  [50], 2, [100, 0.4])
    test_signal_2 = signal_source(0.4, 30, 2,  [50, 10], 3, [100, 10, 0.4])
    test_signal_3 = test_signal = signal_source(0.4, 30, 4,  [50, 8, 0.2], 2, [100, 0.4])
    # 将一组信号合并成一个list
    test_signal = [test_signal_1, test_signal_2, test_signal_3]
    simu_time = 5000
    # 调用merge函数进行测试
    data = merge_signal(test_signal, simu_time)
    # 绘制看一下
    print(data.shape)
    plt.plot(data[100000:1200000])
    plt.show()
    print("开始写入")
    np.savetxt("..\data\mul.txt", data)


# 进行线性调频信号的测试
def test_LFM_singal():
    # 频率捷变的LFM
    test_signal = signal_source(1, 30, 5,  [50, 40, 0.2], 1, [100])
    # 跨帧的大带宽LFM
    test_signal = signal_source(1, 30, 6,  [50, 40, 0.2, 4], 1, [100])
    simu_time = 5000
    # 生成PDW真值
    test_signal.get_plus(simu_time)
    # 生成模拟信号
    test_signal.get_analog_signal()
    # 增加环境噪声
    test_signal.add_channel()
    test_signal.draw(100000, 1200000)
    print("开始写入")
    np.savetxt("..\data\LFM.txt", test_signal.signal)

# 进行多个信号源和合并
def merge_signal(signals, simu_time):
    '''
    :param signals : 需要进行仿真的信号
    :param simu_time: 进行仿真的时间
    '''
    # 首先生成信号0的数据
    signals[0].get_plus(simu_time)
    signals[0].get_analog_signal()
    signals[0].add_channel()
    data = signals[0].signal
    # 将其他信号全部叠加上去
    for i in range(1, len(signals)):
        signals[i].get_plus(simu_time)
        signals[i].get_analog_signal()
        signals[i].add_channel()
        data += signals[i].signal
    return data


if __name__ == "__main__":
    Main()
    print("写入完成")
