# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key = lambda x: x.start)

        res = []

        for interval in intervals:
            if res and res[-1].end >= interval.start:
                res[-1].end = max(res[-1].end, interval.end)
            else:
                res.append(Interval(interval.start, interval.end))

        return res