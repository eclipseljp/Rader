"""
@author:caocongcong
"""

import abc


class PriGenerator(object):
    """
    重频参数产生的函数
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_pri(self):
        pass
