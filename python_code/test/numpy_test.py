from primary_signal.const_value import constValue
from util.Tool import show_Data

__author__ = 'caocongcong'
import numpy as np
if __name__ == "__main__":
    subconde_last_time = 0.02
    subcode_values = [1,0, 0, 1, 0, 0, 1]
    fs = 200
    sample_number = int(constValue.system_freq * subconde_last_time)
    time = np.linspace(0, sample_number, sample_number)
    frame_signal = np.zeros(sample_number * len(subcode_values))
    subcode_signal = np.cos(2 * np.pi * time / (constValue.system_freq / fs))
    for i in range(len(subcode_values)):
        if subcode_values[i] == 0:
            frame_signal[i * sample_number: (i + 1) * sample_number] = subcode_signal
        else:
            frame_signal[i * sample_number: (i + 1) * sample_number] = -subcode_signal
    show_Data(frame_signal)