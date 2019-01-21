"""
@author:caocongcong
"""
from generate_signal.genrate_pri.pri_generate_implament.pri_param_method import pri_param_method

class generate_fixed_method(pri_param_method):
    '''
    进行固定重频的生成
    '''
    def __init__(self):
        # 最终生成的重频数据
        self.pri_data = None

    def generate_pri(self, simutime, pw, param):
        # 生成重频的过程
        self.pri_data = "generate by fixed"

    def get_pri_data(self):
        return self.pri_data