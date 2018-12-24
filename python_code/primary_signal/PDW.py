__author__ = 'caocongcong'


class PDW:
    def __init__(self, begin_time, begin_fs, end_fs, pw, DOA, PA = 1):
        '''
        脉冲描述字类，传入的参数包括起始时间、起始频率、截至频率、脉宽、到达角
        :param begin_time: 该脉冲的起始时间
        :param begin_fs: 该脉冲的起始的频率
        :param end_fs: 该脉冲的截至频率
        :param pw: 脉宽
        :param DOA: 到达角
        :return:
        '''
        self.begin_time = begin_time
        self.begin_fs = begin_fs
        self.end_fs = end_fs
        self.pw = pw
        self.DOA = DOA
        self.PA = PA

    def __lt__(self, other):
        '''
        重载了小于运算符，使得可以PWD按时间顺序进行排序
        :param other:
        :return:
        '''
        return self.begin_time < other.begin_time

    def to_list(self):
        '''
        返回一个list,写入csv比较方便
        :return:
        '''
        return [self.begin_time, self.begin_fs, self.end_fs, self.pw, self.DOA, self.PA]


if __name__ == "__main__":
    test1 = PDW(20, 10, 20, 10, 32)
    test2 = PDW(10, 10, 20, 10, 32)
    test3 = PDW(30, 10, 20, 10, 32)
    test = [test1, test2, test3]
    test.sort()
    for tmp in test:
        print(tmp.begin_time)