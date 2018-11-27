__author__ = 'caocongcong'


class DOA():
    def __init__(self, begin_time, doa):
        self.begin_time = begin_time
        self.DOA = doa

    def __lt__(self, other):
        return self.begin_time < other.begin_time


class DOAParam():
    def __init__(self):
        pass