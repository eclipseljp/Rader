__author__ = 'cao'
import numpy as np
import matplotlib.pyplot as plt
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