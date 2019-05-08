"""
@author:caocongcong
"""
from generate_signal.generate_fs.fs_generate_factory.GenerateDiversityFs import GenerateDiversityFs
from generate_signal.generate_fs.fs_generate_factory.GenerateFixedFs import GenerateFixedFs
from generate_signal.generate_fs.fs_generate_factory.GenerateGroupJitterFs import GenerateGroupJitterFs
from generate_signal.generate_fs.fs_generate_factory.GenerateJitterFs import GenerateJitterFs
from generate_signal.signal_enum import FrequencyEnum, RepetitionRateEnum


class FsFactory():
    '''
    Fs参数产生的工厂类
    '''
    def __init__(self):
        self.generator = None

    def generate_fs_param(self, type, params):
        '''
        生成频率参数
        :param type: 类型参数包括固定频率，频率捷变、频率分集、脉组变频
        :param params: 产生频率的具体参数
                      对于 固定频率，参数包括 帧的数目、中心频点
                      对于 脉间捷变，参数包括 帧的数目，中心频点，捷变范围、捷变个数
                      对于 频率分集， 参数包括 帧的数目，频率数组
                      对于 频率脉组变频，参数包括帧的数目，每组脉冲数，脉冲数组
        :return:
        '''
        if type == FrequencyEnum.fs_fixed:
            self.generater = GenerateFixedFs()
            return self.generater.product_pri(params[0], params[1])
        elif type == FrequencyEnum.fs_jitter:
            self.generater = GenerateJitterFs()
            return self.generater.product_pri(params[0], params[1], params[2], params[3])
        elif type == FrequencyEnum.fs_diversity:
            self.generater = GenerateDiversityFs()
            return self.generater.product_pri(params[0], params[1])
        elif type == FrequencyEnum.fs_group_jitter:
            self.generater = GenerateGroupJitterFs()
            return self.generater.product_pri(params[0], params[1], params[2])