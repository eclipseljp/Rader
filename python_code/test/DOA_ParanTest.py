__author__ = 'caocongcong'
from primary_signal.DOA_Param import DOA_Param
if __name__ == "__main__":
    begin_time = [1.2, 1.4, 1.6, 1.7, 1.9, 2.1]
    doas = [12, 14, 16, 17, 19, 21]
    doasTest = DOA_Param(begin_time, doas)
    print(doasTest.findClosest(1.32))