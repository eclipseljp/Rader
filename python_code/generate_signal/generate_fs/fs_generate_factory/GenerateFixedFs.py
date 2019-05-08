"""
@author:caocongcong
"""
from generate_signal.generate_fs.FsGenerator import FsGenerator


class GenerateFixedFs(FsGenerator):
    '''
    进行信号频率生成
    '''
    def product_fs(self, frame_number, fs):
        '''
        进行频率参数生成
        :param frame_number:
        :param fs:
        :return:
        '''
        fs_data = []
        for i in range(frame_number):
            fs_data.append(fs)
        return fs_data


