"""
@author:caocongcong
"""
import abc


class FrameGenerator(object):
    """
       带内信号产生的函数
       """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_frame(self):
        pass