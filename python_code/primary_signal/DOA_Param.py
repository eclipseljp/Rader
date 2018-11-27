__author__ = 'caocongcong'
from bisect import bisect_left

class DOA:

    def __init__(self, begin_time, DOA):
        self.begin_time = begin_time
        self.DOA = DOA

    def __lt__(self, other):
        return self.begin_time < other.begin_time

    def set_begin_time(self, begin_time):
        self.begin_time = begin_time


class DOA_Param:
    def __init__(self, begin_times, doas):
        i = 0
        self.DOAs = []
        while i < len(begin_times):
            self.DOAs.append(DOA(begin_times[i], doas[i]))
            i += 1

    def findClosest(self, doa):
        myDOA = DOA(doa, 0)
        pos = bisect_left(self.DOAs, myDOA)
        print(pos)
        if pos == 0:
            return self.DOAs[0].DOA
        if pos == len(self.DOAs):
            return self.DOAs[-1].DOA

        before = self.DOAs[pos -1]
        after = self.DOAs[pos]

        if after.begin_time - myDOA.begin_time < myDOA.begin_time - before.begin_time:
            return after.DOA
        else:
            return before.DOA
