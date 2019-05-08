"""
@author:caocongcong
"""
from generate_signal.genrate_pri.PriGenerator import PriGenerator


class GenerateIrregularGroupPri(PriGenerator):
    def product_pri(self, simu_time, pw, group_number, signal_pris):
        pri_data = []
        start_time = self.get_start_time(signal_pris[0])
        # 当前时间就是起始时间
        current_time = start_time
        # pri的计数器
        pri_order = 0
        # group 计数器
        group_order = 0

        # pri的个数
        pri_num = len(signal_pris)

        # 当前的pri值
        current_pri = signal_pris[0]

        while current_time < simu_time:
            if group_order < group_number:
                current_time = round(current_time, 2)
                pri_data.append(current_time)
                current_time += (pw + current_pri)
                pri_order += 1
            else:
                if pri_order >= pri_num:
                    pri_order = 0
                current_time = signal_pris[pri_order]
                pri_order += 1
                group_order = 0
        return pri_data
