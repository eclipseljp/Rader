__author__ = 'caocongcong'
from primary_signal.Rada_mode import FS_type, PRI_type
from primary_signal.pluse import pluse
from primary_signal.const_value import constValue
import numpy as np
import random
import matplotlib.pyplot as plt
# 记录信号源的类
class signal_source:
    # 输入参数为脉宽，PRI种类,和主频率种类，以及DOA参数
    def __init__(self, pw, DOA,  FS_type_input,  FS_params, PRI_type_input, PRI_params):
        '''
        :param pw: 该信号的脉宽
        :param PRI_type: 重频的类型
        :param FS_type: 频率的类型
        :param DOA:到达角参数
        :param params: 设置频率的参数，类型为元组
        1、如果类型是固定频率，只有一个参数为频率中心
        2、如果类型是频率捷变，传入参数为两个，第一个参数为频率中心，第二个为捷变范围
        3、如果类型是频率分集，就会传入一个频率数组
        4、如果是频率脉组变频，传入的参数为脉组个数和对应频率
        5、如果是线性调频，传入参数为起始频率，变化范围，捷变范围
        :param PRI_params: 设置重频参数
        1、如果类型是固定重频，只有一个参数为重频
        2、如果是重频参差\抖动，只有一个参数为中心频率，还有参差抖动的范围
        3、如果是重频脉组，就传入三个个参数，分别为脉组个数和对应的重频和变化范围
        :return:
        '''
        self.pw = pw
        self.PRI_type_need = PRI_type_input
        self.FS_type_need = FS_type_input
        self.DOA = DOA
        self.FS_params = FS_params
        self.PRI_params = PRI_params


    # 得到PWD真值,给定给定的类型，生成一个个脉冲的参数， 即脉冲的真值
    def get_plus(self, simu_time):
        '''
        :param simu_time:整体的仿真时间
        :return:
        '''
        # 记录当前的仿真时间
        current_time = 0
        # 保存最后的脉冲数据
        self.signal_pluses = []
        self.simu_time = simu_time
        # 对于不同的情况进行判断，生成对应的PWD字
        # TODO 还有线性调频的信号没有实现
        if FS_type(self.FS_type_need) == FS_type.fs_fixed:
            # 获取频率参数
            signal_fs = self.FS_params[0]

            if PRI_type(self.PRI_type_need) == PRI_type.pri_fixed:
                print("固定频率固定重频")
                # 固定频率固定重频
                # 获取重频参数
                signal_pri = self.PRI_params[0]

                # 首先生成一段不超过PRI的随机时间作为起始时间
                start_time = self.get_start_time(signal_pri)
                # 保留两位
                #print("当前生成的起始时间", start_time)
                current_time = start_time
                # 开始生成信号
                # 当当前的时间不超过仿真的总时间
                while current_time < simu_time:
                    # 生成一个脉冲
                    tmp_pluse = pluse(signal_fs, current_time, self.pw, self.DOA)
                    # 加入到脉冲数组
                    self.signal_pluses.append(tmp_pluse)
                    # 更新时间，调整到下一个的到达时间
                    current_time += (self.pw + signal_pri)

            elif PRI_type(self.PRI_type_need) == PRI_type.pri_irre:
                # 重频为抖动的情况下
                print("固定频率和抖动重频")
                # 获取重频的中心频点和抖动范围
                signal_pri = self.PRI_params[0]
                signal_pri_range = self.PRI_params[1]

                # 首先生成一段不超过PRI的随机时间作为起始时间
                start_time = self.get_start_time(signal_pri)
                # 保留两位
                current_time = start_time
                while current_time < simu_time:
                    tmp_pluse = pluse(signal_fs, current_time, self.pw, self.DOA)
                    self.signal_pluses.append(tmp_pluse)
                    # 随机生成与下一个脉冲的间隔时间
                    tmp_prt = signal_pri* (1 + random.random() * signal_pri_range - (signal_pri_range/2))
                    current_time += (self.pw + tmp_prt)
            else:
                print("固定频率和脉组")
                # 获取重频的参数,依次为中心重频、脉组数目、重频变化范围
                # 获取信号的重频中心
                signal_pri = self.PRI_params[0]
                # 获取重频的脉组个数
                pri_num = self.PRI_params[1]
                # 重频的变化范围
                signal_pri_range = self.PRI_params[2]
                # 首先生成一段不超过PRI的随机时间作为起始时间
                start_time = self.get_start_time(signal_pri)
                # 当前时间就是起始时间
                current_time = start_time
                # pri的计数器
                pri_order = 0
                tmp_prt = signal_pri* (1 + random.random() * signal_pri_range - (signal_pri_range/2))
                while current_time < simu_time:
                    if (pri_order < pri_num):
                        # 使用当前的重频不变
                        tmp_pluse = pluse(signal_fs, current_time, self.pw, self.DOA)
                        self.signal_pluses.append(tmp_pluse)
                        current_time += self.pw + tmp_prt
                        pri_order += 1
                        # 输出进行测试
                        # print("当前时间：", current_time)
                        # print("脉组order:", pri_order)
                        # print("当前重频:", tmp_prt)
                    else:
                        # 生成新的重频
                        tmp_prt = signal_pri* (1 + random.random() * signal_pri_range - (signal_pri_range/2))
                        # pri的计数器清零
                        pri_order = 0
        elif FS_type(self.FS_type_need) == FS_type.fs_agile:
            # 频率捷变情况
            # 获取频率参数
            # 起始频率
            signal_fs = self.FS_params[0]
            # 范围，单位为Mhz
            signal_fs_range = self.FS_params[1]
            if PRI_type(self.PRI_type_need) == PRI_type.pri_fixed:
                print("频率捷变固定重频")
                # 固定频率固定重频
                # 获取重频参数
                signal_pri = self.PRI_params[0]
                # 首先生成一段不超过PRI的随机时间作为起始时间
                start_time = self.get_start_time(signal_pri)
                # 保留两位
                #print("当前生成的起始时间", start_time)
                current_time = start_time
                # 开始生成信号
                # 当当前的时间不超过仿真的总时间
                while current_time < simu_time:
                    # 生成一个脉冲
                    tmp_fs = signal_fs + random.random()*signal_fs_range
                    tmp_pluse = pluse(tmp_fs, current_time, self.pw, self.DOA)
                    # 加入到脉冲数组
                    self.signal_pluses.append(tmp_pluse)
                    # 更新时间，调整到下一个的到达时间
                    current_time += (self.pw + signal_pri)

            elif PRI_type(self.PRI_type_need) == PRI_type.pri_irre:
                # 重频为抖动的情况下
                print("频率捷变和抖动重频")
                # 获取重频的中心频点和抖动范围
                signal_pri = self.PRI_params[0]
                signal_pri_range = self.PRI_params[1]

                # 首先生成一段不超过PRI的随机时间作为起始时间
                start_time = self.get_start_time(signal_pri)
                # 保留两位
                current_time = start_time
                while current_time < simu_time:
                    tmp_fs = signal_fs + random.random()*signal_fs_range
                    tmp_pluse = pluse(tmp_fs, current_time, self.pw, self.DOA)
                    self.signal_pluses.append(tmp_pluse)
                    # 随机生成与下一个脉冲的间隔时间
                    tmp_prt = signal_pri* (1 + random.random() * signal_pri_range - (signal_pri_range/2))
                    current_time += (self.pw + tmp_prt)
            else:
                print("频率捷变和脉组重频")
                # 获取重频的参数,依次为中心重频、脉组数目、重频变化范围
                # 获取信号的重频中心
                signal_pri = self.PRI_params[0]
                # 获取重频的脉组个数
                pri_num = self.PRI_params[1]
                # 重频的变化范围
                signal_pri_range = self.PRI_params[2]
                # 首先生成一段不超过PRI的随机时间作为起始时间
                start_time = self.get_start_time(signal_pri)
                # 当前时间就是起始时间
                current_time = start_time
                # pri的计数器
                pri_order = 0
                tmp_prt = signal_pri* (1 + random.random() * signal_pri_range - (signal_pri_range/2))
                while current_time < simu_time:
                    if (pri_order < pri_num):
                        # 使用当前的重频不变
                        tmp_fs = signal_fs + random.random()*signal_fs_range
                        tmp_pluse = pluse(tmp_fs, current_time, self.pw, self.DOA)
                        self.signal_pluses.append(tmp_pluse)
                        current_time += self.pw + tmp_prt
                        pri_order += 1
                        # 输出进行测试
                        # print("当前时间：", current_time)
                        # print("脉组order:", pri_order)
                        # print("当前重频:", tmp_prt)
                    else:
                        # 生成新的重频
                        tmp_prt = signal_pri* (1 + random.random() * signal_pri_range - (signal_pri_range/2))
                        # pri的计数器清零
                        pri_order = 0
        elif FS_type(self.FS_type_need) == FS_type.fs_diversity:
            # 频率分集情况
            # 获取频率参数
            # 传进来的频率是一个数组
            signal_fs = self.FS_params
            if PRI_type(self.PRI_type_need) == PRI_type.pri_fixed:
                print("频率分集固定重频")
                # 固定频率固定重频
                # 获取重频参数
                signal_pri = self.PRI_params[0]
                # 首先生成一段不超过PRI的随机时间作为起始时间
                start_time = self.get_start_time(signal_pri)
                # 保留两位
                #print("当前生成的起始时间", start_time)
                current_time = start_time
                # 开始生成信号
                # 当当前的时间不超过仿真的总时间
                fs_order = 0
                while current_time < simu_time:
                    # 生成一个脉冲
                    tmp_fs = signal_fs[fs_order]
                    fs_order += 1
                    tmp_pluse = pluse(tmp_fs, current_time, self.pw, self.DOA)
                    # 加入到脉冲数组
                    self.signal_pluses.append(tmp_pluse)
                    # 更新时间，调整到下一个的到达时间
                    current_time += (self.pw + signal_pri)

                    # 如果选满了，就重新开始
                    if fs_order == len(signal_fs):
                        fs_order = 0

            elif PRI_type(self.PRI_type_need) == PRI_type.pri_irre:
                # 重频为抖动的情况下
                print("频率分集和抖动重频")
                # 获取重频的中心频点和抖动范围
                signal_pri = self.PRI_params[0]
                signal_pri_range = self.PRI_params[1]

                # 首先生成一段不超过PRI的随机时间作为起始时间
                start_time = self.get_start_time(signal_pri)
                # 保留两位
                current_time = start_time
                fs_order = 0
                while current_time < simu_time:
                    tmp_fs = signal_fs[fs_order]
                    fs_order += 1
                    tmp_pluse = pluse(tmp_fs, current_time, self.pw, self.DOA)
                    self.signal_pluses.append(tmp_pluse)
                    # 随机生成与下一个脉冲的间隔时间
                    tmp_prt = signal_pri* (1 + random.random() * signal_pri_range - (signal_pri_range/2))
                    current_time += (self.pw + tmp_prt)
                    if fs_order == len(signal_fs):
                        fs_order = 0

            else:
                print("频率分集和脉组重频")
                # 获取重频的参数,依次为中心重频、脉组数目、重频变化范围
                # 获取信号的重频中心
                signal_pri = self.PRI_params[0]
                # 获取重频的脉组个数
                pri_num = self.PRI_params[1]
                # 重频的变化范围
                signal_pri_range = self.PRI_params[2]
                # 首先生成一段不超过PRI的随机时间作为起始时间
                start_time = self.get_start_time(signal_pri)
                # 当前时间就是起始时间
                current_time = start_time
                # pri的计数器
                pri_order = 0
                tmp_prt = signal_pri* (1 + random.random() * signal_pri_range - (signal_pri_range/2))
                fs_order = 0
                while current_time < simu_time:
                    if (pri_order < pri_num):
                        # 使用当前的重频不变
                        tmp_fs = signal_fs[fs_order]
                        fs_order += 1
                        tmp_pluse = pluse(tmp_fs, current_time, self.pw, self.DOA)
                        self.signal_pluses.append(tmp_pluse)
                        current_time += self.pw + tmp_prt
                        pri_order += 1
                        # 输出进行测试
                        # print("当前时间：", current_time)
                        # print("脉组order:", pri_order)
                        # print("当前重频:", tmp_prt)
                    else:
                        # 生成新的重频
                        tmp_prt = signal_pri * (1 + random.random() * signal_pri_range - (signal_pri_range/2))
                        # pri的计数器清零
                        pri_order = 0
                    if fs_order == len(signal_fs):
                        fs_order = 0
        elif FS_type(self.FS_type_need) == FS_type.fs_pluse_group_conversion:
            # 频率脉组捷变情况
            # 参数有三个，分别是中心频率，脉组个数，变化范围
            signal_fs = self.FS_params[0]
            signal_fs_number = self.FS_params[1]
            signal_fs_range = self.FS_params[2]
            tmp_fs = signal_fs * (1 + random.random()*signal_fs_range - (signal_fs_range/2))

            if PRI_type(self.PRI_type_need) == PRI_type.pri_fixed:
                print("频率脉组捷变固定重频")
                # 固定频率固定重频
                # 获取重频参数
                signal_pri = self.PRI_params[0]
                # 首先生成一段不超过PRI的随机时间作为起始时间
                start_time = self.get_start_time(signal_pri)
                # 保留两位
                #print("当前生成的起始时间", start_time)
                current_time = start_time
                # 开始生成信号
                # 当当前的时间不超过仿真的总时间
                fs_number_order = 0
                while current_time < simu_time:
                    # 生成一个脉冲
                    tmp_pluse = pluse(tmp_fs, current_time, self.pw, self.DOA)
                    # 加入到脉冲数组
                    self.signal_pluses.append(tmp_pluse)
                    # 当前计数+1
                    fs_number_order += 1
                    # 更新时间，调整到下一个的到达时间
                    current_time += (self.pw + signal_pri)

                    # 如果选满了，就重新开始
                    if fs_number_order == signal_fs_number:
                        fs_order = 0
                        # 重新生成新的频率
                        tmp_fs = signal_fs * (1 + random.random()*signal_fs_range - (signal_fs_range/2))

            elif PRI_type(self.PRI_type_need) == PRI_type.pri_irre:
                # 重频为抖动的情况下
                print("频率脉组捷变和抖动重频")
                # 获取重频的中心频点和抖动范围
                signal_pri = self.PRI_params[0]
                signal_pri_range = self.PRI_params[1]

                # 首先生成一段不超过PRI的随机时间作为起始时间
                start_time = self.get_start_time(signal_pri)
                # 保留两位
                current_time = start_time
                while current_time < simu_time:
                    fs_number_order = 0
                    tmp_pluse = pluse(tmp_fs, current_time, self.pw, self.DOA)
                    self.signal_pluses.append(tmp_pluse)
                    # 当前计数+1
                    fs_number_order += 1
                    # 随机生成与下一个脉冲的间隔时间
                    tmp_prt = signal_pri* (1 + random.random() * signal_pri_range - (signal_pri_range/2))
                    current_time += (self.pw + tmp_prt)
                     # 如果选满了，就重新开始
                    if fs_number_order == signal_fs_number:
                        fs_order = 0
                        # 重新生成新的频率
                        tmp_fs = signal_fs * (1 + random.random()*signal_fs_range - (signal_fs_range/2))

            else:
                print("频率脉组捷变和脉组重频")
                # 获取重频的参数,依次为中心重频、脉组数目、重频变化范围
                # 获取信号的重频中心
                signal_pri = self.PRI_params[0]
                # 获取重频的脉组个数
                pri_num = self.PRI_params[1]
                # 重频的变化范围
                signal_pri_range = self.PRI_params[2]
                # 首先生成一段不超过PRI的随机时间作为起始时间
                start_time = self.get_start_time(signal_pri)
                # 当前时间就是起始时间
                current_time = start_time
                # pri的计数器
                pri_order = 0
                tmp_prt = signal_pri* (1 + random.random() * signal_pri_range - (signal_pri_range/2))
                while current_time < simu_time:
                    fs_number_order = 0
                    if (pri_order < pri_num):
                        # 使用当前的重频不变
                        tmp_pluse = pluse(tmp_fs, current_time, self.pw, self.DOA)
                        self.signal_pluses.append(tmp_pluse)
                        fs_number_order += 1
                        current_time += self.pw + tmp_prt
                        pri_order += 1
                        # 输出进行测试
                        # print("当前时间：", current_time)
                        # print("脉组order:", pri_order)
                        # print("当前重频:", tmp_prt)

                    else:
                        # 生成新的重频
                        tmp_prt = signal_pri* (1 + random.random() * signal_pri_range - (signal_pri_range/2))
                        # pri的计数器清零
                        pri_order = 0
                    if fs_number_order == signal_fs_number:
                        fs_order = 0
                        # 重新生成新的频率
                        tmp_fs = signal_fs * (1 + random.random()*signal_fs_range - (signal_fs_range/2))

    # 生成随机的起始时间
    def get_start_time(self, signal_pri):
        # 随机生成一个小于重频的时间做为起始时间
        start_time = random.random() * signal_pri
        # 保留两位小数
        start_time = round(start_time, 2)
        return start_time

    # 获得模拟信号
    def get_analog_signal(self):
        # 总共产生的点数
        # 计算方式为采样仿真时间*系统采样频率
        total_num = int(self.simu_time * constValue.system_freq)
        #print(total_num)
        self.signal = np.zeros(total_num)
        for tmp_pluse in self.signal_pluses:
            # 让当前的脉冲生成模拟信号

            tmp_pluse.get_analog_signal()
            # 获取模拟信号
            tmp_signal = tmp_pluse.plus_signal
            # 当前生成信号的长度
            lenght = tmp_signal.shape[0]
            # 根据当前时间计算偏执
            bias = int(tmp_pluse.begin_time * constValue.system_freq)
            # 叠加到原始信号上
            self.signal[bias: bias+lenght] += tmp_signal

        # 对于线性调频信号单独处理
        current_time = 0
        if FS_type(self.FS_type_need) == FS_type.LFM:
            # 如果是LFM信号，进行模拟信号生成
            # 此时肯定是固定重频
            # 参数有两个，起始频率f0，频率变化范围B， K = B/T
            # 获取重频
            signal_pri = self.PRI_params[0]
            # 获取线性调频的相关参数
            begin_fs = self.FS_params[0]
            # 线性调频宽度
            Band = self.FS_params[1]
            # 起始频率的捷变范围
            fs_range = self.FS_params[2]
            # 计算斜率
            K = Band / self.pw
            # 获取起始时间
            current_time = self.get_start_time(signal_pri)
            while current_time < self.simu_time:
                tmp_fs = begin_fs*(1+random.random()*fs_range - fs_range/2)
                tmp_signal = self.get_LFM(tmp_fs, K, self.pw)
                # 当前生成信号的长度
                lenght = tmp_signal.shape[0]
                # 根据当前时间计算偏执
                bias = int(current_time * constValue.system_freq)
                # 叠加到原始信号上
                self.signal[bias: bias+lenght] += tmp_signal
                # 更新起始时间
                current_time += self.pw + signal_pri
        elif FS_type(self.FS_type_need) == FS_type.lager_bandwidth_LFM:
            # 对于大脉宽信号
            # 此时肯定是固定重频
            # 参数有三个，起始频率f0，频率变化范围B， K = B/T， 跨的帧数n
            # 获取重频
            signal_pri = self.PRI_params[0]
            # 获取线性调频的相关参数
            begin_fs = self.FS_params[0]
            # 线性调频宽度
            Band = self.FS_params[1]
            # 起始频率的捷变范围
            fs_range = self.FS_params[2]
            # 帧数
            fs_frame_number = self.FS_params[3]
            # 计算斜率
            K = Band / (self.pw * fs_frame_number)
            # 获取起始时间
            current_time = self.get_start_time(signal_pri)
            # 当前的frame的序号
            frame_order = 0
            # 一帧的频率跨度
            frame_fs_change = Band / fs_frame_number
            used_fs = begin_fs + frame_fs_change * frame_order
            while current_time < self.simu_time:
                tmp_fs = used_fs*(1+random.random()*fs_range - fs_range/2)
                frame_order += 1
                tmp_signal = self.get_LFM(tmp_fs, K, self.pw)
                # 当前生成信号的长度
                lenght = tmp_signal.shape[0]
                # 根据当前时间计算偏执
                bias = int(current_time * constValue.system_freq)
                # 叠加到原始信号上
                self.signal[bias: bias+lenght] += tmp_signal
                # 更新起始时间
                current_time += self.pw + signal_pri

                # 一组帧已经循环完毕
                if frame_order == fs_frame_number:
                    frame_order = 0
                # 跟新新的当前的起始频率
                used_fs = begin_fs + frame_fs_change * frame_order







    # 增加信道噪声
    def add_channel(self, SNR = 0):
        '''
        :param SNR:信道的信噪比
        :return:
        '''
        # TODO 选择不同的信道，此处只实现了AWGN
        self.AWGN(SNR)


    def AWGN(self, SNR):
        '''
        :param SNR:环境信噪比
        :return:
        '''
        # 将SNR由dB单位转化成倍数关系
        snr = 10**(SNR/10.0)
        # 计算原始信号功率
        xpower = np.sum(self.signal**2)/len(self.signal)
        # 根据信噪比计算已经增加的噪声的功率
        npower = xpower / snr
        # 随机生成噪声
        noise =  np.random.randn(len(self.signal)) * np.sqrt(npower)
        # 将噪声叠加到原始信号上去
        self.signal += noise
    # 绘制信号
    def draw(self, number_begin, number_end):
        '''
        :param number: 绘制信号的点数
        :return:
        '''
        plt.plot(self.signal[number_begin:number_end])
        plt.show()

    # 进行线性调频信号的生成
    def get_LFM(self, begin_fs, k, pw):
        '''
        :param begin_fs:起始频率
        :param k: 频率变化斜率
        :param pw: 信号的脉宽
        :return:生成的信号
        计算公式是: sin(2*pi*f0*t + pi*k*t*t)
        '''
        # 采样的点数
        N = pw * constValue.system_freq
        # 采样时间
        t = np.linspace(0, pw, N)
        signal = np.sin(2*np.pi*begin_fs*t + np.pi*k*t*t)
        return signal
if __name__ == "__main__":
    pass

