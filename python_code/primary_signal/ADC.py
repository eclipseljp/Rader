__author__ = 'caocongcong'

from primary_signal.const_value import constValue
import numpy as np

# 进行信号的采样

class AD:
    def __init__(self, primary_signal, simu_time, frame_time):
        '''
        进行信号的AD采样，首先对原始信号的进行划分，按照帧长划分成子段
        对每个子段进行下变频，然后进行滤波以及重采样
        对每个子信道进行下变频，滤波进行重采样
        汇总每个子带计算的参数进行合并
        :param primary_signal 原始的信号
        :param simu_time 整体系统的仿真时间
        :frame_time 一帧的时间
        '''
        # 原始信号
        # 恢复成不是正信号
        self.primary_signal = primary_signal*2-1
        # 系统整体的仿真时间
        self.simu_time = simu_time
        # 帧的时长
        self.frame_time = frame_time
        # 计算的帧数
        self.frame_number = self.simu_time / self.frame_time
        # 每帧的数目
        self.frame_sample_number = int (self.frame_time * constValue.system_freq)




    def split_signal(self):
        '''
        进行信号初步划分，将仿真时间内的信号划分成几个子段，每个子段的长度为帧的frame_sample_number
        :return: 更新split_signal_data
        '''
        # 保存切分后的数据
        self.split_signal_data = []
        # 当前划分到的数据下标
        current_index = 0
        # 当没有划分完毕的时候
        while current_index < len(self.primary_signal):
            # 说明取到了最后一行，此时直接全部加入
            if current_index + self.frame_sample_number < len(self.primary_signal):
                # 全部加入
                tmp = self.primary_signal[current_index:]
                self.split_signal_data.append(tmp)
                # 退出循环
                break

            # 每次截取采样长度的点
            tmp = self.primary_signal[current_index: current_index+self.frame_sample_number]
            # 当前位置递增
            current_index += self.frame_sample_number
            # 加到最后
            self.split_signal_data.append(tmp)


    def down_conversion(Mode, conbersion_fs, sample_fs, input_data):
        '''
        进行下变频，转化到自己所需要的频率
        :param Mode: 是I路还是Q路，决定乘以sin还是cos
        :param conbersion_fs: 转到的频率
        :param sample_fs: 采样频率
        :param input_data :输入数据
        :return: 变频之后的数据
        '''
        if Mode == "Sin":
            # 产生等长sin的信号
            t = np.linspace(0, len(input_data), len(input_data))
            changed_signal = np.sin(2*np.pi*t/(sample_fs/conbersion_fs))
            # 对原始信号进行变化
            changed_signal *= input_data
        else:
            # 产生等长cos的信号
            t = np.linspace(0, len(input_data), len(input_data))
            changed_signal = np.cos(2*np.pi*t/(sample_fs/conbersion_fs))
            # 对原始信号进行变化
            changed_signal *= input_data

        return changed_signal

    def FIR_filter(self, Mode):
        '''
        低通滤波器，进行滤波处理，实际只有400M和60M两种选择
        :param Mode: 只有两种选择，为400M和60M
        :return:
        '''
        pass