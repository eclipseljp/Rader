__author__ = 'caocongcong'
from primary_signal.const_value import constValue
import scipy.signal as signal
import pylab as pl
import numpy as np
if __name__ == "__main__":
    b = np.array(constValue.lp_fs400_Overband20)
    w, h = signal.freqz(b, 1)
    pl.plot(w/2/np.pi, 20*np.log10(np.abs(h)))
    pl.show()