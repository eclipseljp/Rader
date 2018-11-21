__author__ = 'cao'
from util.Tool import show_Data
import  numpy as np
if __name__ == "__main__":
    t = np.linspace(0, 24, 34)
    sample_fs = 60
    fs = 15
    data = np.sin(2*np.pi*fs/sample_fs*t)
    extend = np.zeros(64 - 24)
    data  = np.append(data, extend)

    show_Data(data)