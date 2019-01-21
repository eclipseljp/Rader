"""
@author:caocongcong
"""
from generate_signal.genrate_pri.pri_generate_implament.pri_param_method import pri_param_method


class generate_conv_group_pri(pri_param_method):

    def __init__(self):
        self.pri_data = None

    def generate_pri(self, simutime, pw, param):
        self.pri_data = "generate by conv group"

    def get_pri_data(self):
        return self.pri_data
