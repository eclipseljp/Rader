__author__ = 'caocongcong'
import numpy as np

def draw_primary():
    RF = 2.3*1e7  # 载频230MHz
    PW = 8*1e-5  # 脉冲宽度80us
    PRI = 4*1e-4  # 载波重复周期400us
    PA = 1  # 载波宽度
    per = PW/PRI  # 载波占重复周期的比例
    N = PRI*RF  # 载波重复周期内的完整周期个数

    # 进行信号生成
    t = np.linespace(0, 5*PRI, 20*N)
    

if __name__ == "__main__":
    pass