__author__ = 'caocongcong'
# 保存仿真系统的常量值
class constValue():
    # 系统时钟为1.2GHz 单位为MHz
    system_freq = 2e3

    # 信号频率范围为0.1M到1G测频精度, 1MHz,单位为MHz
    freq_accu = 1
    max_freq = 1e3
    min_freq = 0.1

    # 系统的时间计量单位 us
    # 脉宽的设定, 范围为 0.1us到2毫秒，精度为0.1微秒
    max_pw = 2000
    min_pw = 0.1
    pw_accu = 0.1

    # 脉冲重复周期 PRI，范围2到10000us,精度为0.2微秒
    max_PRI = 10000
    min_PRI = 2
    PRI_accu = 0.2

    # 到达角参数，手动测定，测量精度为3度
    DOA_accu = 3

    # 滤波器参数设置
    first_fluter_base = 200
    first_fluter_pass = 30
    first_fluter_length = 30
    second_fluter_base = 15
    second_fluter_pass = 3
    second_fluter_length = 15

    # 采样频率设置
    first_sample_fs = 480
    second_sample_fs = 60
    second_base_fs = [-185 ,  -155 ,  -125 ,  -95 ,  -65 ,  -35 ,  -5 ,  25 ,  55 ,  85 ,  115 ,  145 ,  175 ,  205]

    # 进行检波的时候连续多少个超过门限
    detect_number = 10
    # 计算FFT使用的点数
    fft_number = 60