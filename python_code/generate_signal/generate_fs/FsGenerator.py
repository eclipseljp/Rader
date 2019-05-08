"""
@author:caocongcong
"""
import abc


class FsGenerator():
    """
        频率产生的函数
        """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_fs(self):
        pass
