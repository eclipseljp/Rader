
"""
@author:caocongcong
"""
from generate_signal.constant.frame_type_enum import frame_type_enum
from generate_signal.generate_frame_signal.frame_genrate_implament.generate_single_frame import generate_single_frame
from generate_signal.generate_frame_signal.frame_genrate_implament.genrate_lfm_frame import genrate_lfm_signal
class frame_generate_factory:
    def __int__(self):
        self.generator = None

    def genrate_frame_generator(self, type):
        if type == frame_type_enum.single_fs:
            self.generator = generate_single_frame()
        elif type == frame_type_enum.lfm:
            self.generator = genrate_lfm_signal()
        return self.generator
