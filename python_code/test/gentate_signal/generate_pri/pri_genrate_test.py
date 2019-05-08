"""
@author:caocongcong
"""
from generate_signal.genrate_pri.PriFactory import pri_factory
from generate_signal.constant.pri_type_enum import PRI_type_enum


class pri_factory_test():
    def pri_generate(self):
        used_pri_factory = pri_factory()
        pri_genrator = used_pri_factory.generate_pri_param(PRI_type_enum.pri_uneven)
        simutime = 200
        pw = 1
        param = [[19, 20, 21]]
        pri_genrator.generate_pri(simutime, pw, param)
        print(pri_genrator.get_pri_data())
        print("观察差分输出")
        pri_data = pri_genrator.get_pri_data()
        for i in range(1, len(pri_data)):
            print(pri_data[i] - pri_data[i - 1])


if __name__ == "__main__":
    pri_factory_test_example = pri_factory_test()
    pri_factory_test_example.pri_generate()
