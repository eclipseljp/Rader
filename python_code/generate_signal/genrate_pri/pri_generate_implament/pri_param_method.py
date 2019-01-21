"""
@author:caocongcong
"""
from abc import ABCMeta, abstractmethod


class pri_param_method(metaclass=ABCMeta):
    @abstractmethod()
    def generate_pri(self, simutime, pw, param):
        pass

    @abstractmethod
    def get_pri_data(self):
        pass
