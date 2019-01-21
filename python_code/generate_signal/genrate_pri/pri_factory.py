"""
@author:caocongcong
"""
from generate_signal.genrate_pri.pri_generate_implament.generate_fixed_pri import generate_fixed_method
from generate_signal.genrate_pri.pri_generate_implament.generate_irre_pri import generate_irre_pri
from generate_signal.genrate_pri.pri_generate_implament.generate_uneven_pri import generate_uneven_pri
from generate_signal.genrate_pri.pri_generate_implament.generate_conv_group_pri import generate_conv_group_pri
from generate_signal.constant.pri_type_enum import PRI_type_enum


class pri_factory:
    def __init__(self):
        self.generater = None

    def generate_pri_param(self, type):
        if type == PRI_type_enum.pri_fixed:
            self.generater = generate_fixed_method()
        elif type == PRI_type_enum.pri_irre:
            self.generater = generate_irre_pri()
        elif type == PRI_type_enum.pri_uneven:
            self.generater = generate_uneven_pri()
        elif type == PRI_type_enum.pri_group_conversion:
            self.generater = generate_conv_group_pri()
        ## TODO 异常处理
        return self.generater
