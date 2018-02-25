# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        end = intervals[0].end
        res = 0

        for itv in intervals[1:]:
            if itv.start < end:
                res += 1
                end = min(itv.end, end)
            else:
                end = itv.end