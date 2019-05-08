"""
@author:caocongcong
"""
from generate_signal.generate_fs.FsGenerator import FsGenerator


class GenerateDiversityFs(FsGenerator):
    '''
    分集信号
    '''
    def product_fs(self, frame_number, fs_values):
        '''
        频率分集信号的产生
        :param frame_number:
        :param fs_values:
        :return:
        '''
        fs_data = []
        fs_order = 0
        for i in range(frame_number):
            if fs_order == len(fs_values):
                fs_order = 0
            fs_data.append(fs_values[fs_order])
        return fs_data