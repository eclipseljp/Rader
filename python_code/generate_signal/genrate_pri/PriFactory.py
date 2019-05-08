"""
@author:caocongcong
"""
from generate_signal.genrate_pri.pri_generate_implament.GenerateFixedPri import GenerateFixedPri
from generate_signal.genrate_pri.pri_generate_implament.GenerateJitterPri import GenerateJitterPri
from generate_signal.genrate_pri.pri_generate_implament.GenerateIrregularPri import GenerateIrregular
from generate_signal.genrate_pri.pri_generate_implament.GenerateIrregularGroupPri import GenerateIrregularGroupPri
from generate_signal.signal_enum import RepetitionRateEnum


class pri_factory:
    def __init__(self):
        self.generater = None

    def generate_pri_param(self, type, params):
        '''
        进行雷达的PRI参数生成
        :param type: 消息类别 包括 重频固定、重频捷变、重频脉组参差、重频参差
        :param params: 消息的具体参数
                        对于固定重频，参数依次为 仿真时间、脉宽和PRI值
                        对于重频参差， 参数依次为 仿真时间、脉宽、参差的PRI数组
                        对于重频抖动，参数依次为 仿真时间、脉宽、PRI中心值、PRI抖动值、PRI抖动个数
                        对于脉组参差，参数依次为 仿真时间、脉宽、脉组个数和参差的PRI数组
                        对于所有的类别，最后一个值为起始时间，如果为0，就随机分配
        :return:
        '''
        # TODO 对输入参数进行异常检查
        if type == RepetitionRateEnum.pri_fixed:
            self.generater = GenerateFixedPri()
            return self.generater.product_pri(params[0], params[1], params[2], params[3])
        elif type == RepetitionRateEnum.pri_jitter:
            self.generater = GenerateJitterPri()
            return self.generater.product_pri(params[0], params[1], params[2], params[3], params[4], params[5])
        elif type == RepetitionRateEnum.pri_irregular:
            self.generater = GenerateIrregular()
            return self.generater.product_pri(params[0], params[1], params[2], params[3])
        elif type == RepetitionRateEnum.pri_group_irregular:
            self.generater = GenerateIrregularGroupPri()
            return self.generater.product_pri(params[0], params[1], params[2], params[3], params[4])
