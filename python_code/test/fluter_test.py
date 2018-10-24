__author__ = 'caocongcong'
from primary_signal.const_value import constValue
import scipy.signal as signal
import pylab as plt
import numpy as np
if __name__ == "__main__":
    b = np.array(constValue.lp_fs400_Overband20)
    w, h = signal.freqz(b, 1)
    plt.plot(w/2/np.pi, 20*np.log10(np.abs(h)))
    plt.show()
    # 进行滤波实验
    fs = 1.2e9
    f1 = 0.2e9
    f2 = 0.5e9
    time = 0.000001
    t = np.linspace(0, time, int(time*fs))
    s = np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)
    plt.plot(t, s)
    plt.xlabel('time/s')
    plt.title('before fliter')
    plt.show()
    sf = signal.filtfilt(b, 1, s)
    plt.plot(t, sf)
    plt.xlabel('time/s')
    plt.title('after fliter')
    plt.show()

