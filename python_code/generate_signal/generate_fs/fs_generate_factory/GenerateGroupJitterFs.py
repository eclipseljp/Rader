"""
@author:caocongcong
"""
from generate_signal.generate_fs.FsGenerator import FsGenerator


class GenerateGroupJitterFs(FsGenerator):
    def product_fs(self, frame_number, group_number, fs_values):
        fs_data = []
        group_order = 0
        fs_order = 0
        current_fs = fs_values[fs_order]
        for i in range(frame_number):
            if group_order < group_number:
                fs_data.append(current_fs)
            else:
                if fs_order == len(fs_values):
                    fs_order = 0
                current_fs = fs_values[fs_order]
                group_order = 0
        return fs_data
