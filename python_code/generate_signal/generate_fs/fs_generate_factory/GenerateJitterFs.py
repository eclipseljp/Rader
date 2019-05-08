"""
@author:caocongcong
"""
import random

from generate_signal.generate_fs.FsGenerator import FsGenerator


class GenerateJitterFs(FsGenerator):

    def get_next_fs(self, fs_value, jitter_value, jitter_number):
        '''
        根据捷变参数生成下一个频率参数
        :param pri_value:  原始的频率参数
        :param jitter_value: 捷变的范围
        :param jitter_number:  捷变的个数
        :return: 返回下一个频率
        '''
        if jitter_number <= 0:
            return random.randrange(fs_value - jitter_value, fs_value + jitter_value, 1)
        else:
            return random.randrange(fs_value - jitter_value, fs_value + jitter_value,
                                    round((jitter_value * 2 + 0.0) / jitter_number))

    def product_fs(self, frame_number, fs_value, jitter_value, jitter_number):
        '''
        生成捷变的频率序列
        :param frame_number: 需要生成的频率个数
        :param fs_value: 中心频点
        :param jitter_value: 捷变的范围
        :param jitter_number: 捷变个数
        :return:
        '''
        fs_data = []
        for i in range(frame_number):
            fs_data.append(self.get_next_fs(fs_value, jitter_value, jitter_number))
        return fs_data
