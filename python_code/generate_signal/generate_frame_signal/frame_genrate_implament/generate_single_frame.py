"""
@author:caocongcong
"""
from generate_signal.generate_frame_signal.frame_genrate_implament.generate_frame_method import generate_frame_method
from primary_signal.const_value import constValue
import numpy as np

class generate_single_frame(generate_frame_method):
    def __init__(self):
        self.plus_signal = None

    def generate_frame_data(self, param, pw):
        fs = param[0]
        sample_number = int(constValue.system_freq * pw)
        time = np.linspace(0, sample_number, sample_number)
        self.plus_signal = np.sin(2 * np.pi * time / (constValue.system_freq / fs))

    def get_priamary_data(self):
        return self.plus_signal