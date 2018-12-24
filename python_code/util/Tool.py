__author__ = 'cao'
import numpy as np
import matplotlib.pyplot as plt
import csv
# 一些工具的使用

# 展示数据的频率和时域
def show_Data(primary_data):
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(primary_data)
    # ax1.title("primary signal in time demain")
    ax2 = fig.add_subplot(2, 1, 2)
    w = np.linspace(0, 2 * np.pi, len(primary_data))
    ax2.plot(w, np.abs(np.fft.fft(primary_data)))
    plt.show()

def show_complex(primary_data):
    fig = plt.figure()
    ax0 = fig.add_subplot(3, 1, 1)
    ax0.plot(np.abs(primary_data))
    # ax1.title("primary signal in time demain")
    ax1 = fig.add_subplot(3, 1, 2)
    ax1.plot(np.real(primary_data))
    ax2 = fig.add_subplot(3, 1, 3)
    w = np.linspace(0, 2 * np.pi, len(primary_data))
    ax2.plot(w, np.abs(np.fft.fft(primary_data)))
    plt.show()

def show_data_mean(primary_data):
    fig = plt.figure()
    plt.plot(primary_data)
    mean = np.mean(primary_data)*np.ones(primary_data.shape)
    plt.plot(mean)
    plt.show()

def show_data_cursor(primary_data, cursors):
    fig = plt.figure()
    index = np.linspace(0, len(primary_data), len(primary_data))
    plt.plot(index, primary_data)
    max_value = max(primary_data)
    min_value = min(primary_data)
    for cursor in cursors:
        # print(cursor)
        # print([cursor[0], cursor[0]])

        plt.plot([cursor[0], cursor[0]] , [min_value, max_value], "r")
        plt.plot( [cursor[1], cursor[1]], [min_value, max_value], "r")
    plt.show()

def write_PDW(file_path, data):
    # 首先对PDW进行排序
    data.sort()
    # 开始写入PDW参数
    print("开始写入参数")
    header = ["begin_time", "begin_fs", "end_fs", "pw", "DOA", "PA"]
    with open(file_path, 'w', newline='') as f:
        writter = csv.writer(f)
        # 首先写入频率参数
        writter.writerow(header)
        for tmp_pdw in data:
            param_list = tmp_pdw.to_list()
            writter.writerow(param_list)
    print("参数写入完毕")
