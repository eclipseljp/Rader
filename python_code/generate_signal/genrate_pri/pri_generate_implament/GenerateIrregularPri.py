"""
@author:caocongcong
"""
from generate_signal.genrate_pri.PriGenerator import PriGenerator


class GenerateIrregular(PriGenerator):
    '''
    进行捷变雷达生成
    '''

    def product_pri(self, simu_time, pw, signal_pris):
        '''
        进行PRI生成
        :param simu_time: 仿真的总体时间
        :param pw: 脉宽
        :param signal_pris: 参差的pri的具体值
        :return: 具体的PRI序列
        '''
        pri_data = []
        start_time = self.get_start_time(signal_pris[0])
        # 当前时间就是起始时间
        current_time = start_time
        # pri的计数器
        pri_order = 0
        pri_num = len(signal_pris)
        while current_time < simu_time:
            if (pri_order < pri_num):
                # 使用当前的重频不变
                current_time = round(current_time, 2)
                pri_data.append(current_time)
                current_time += (pw + signal_pris[pri_order])
                pri_order += 1
            else:
                # pri的计数器清零
                pri_order = 0
        return pri_data
