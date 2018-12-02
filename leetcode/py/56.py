class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key = lambda itv: itv.start)

        res = []
        for itv in intervals:
            if res and res[-1].end >= itv.start:
                res[-1].end = max(res[-1].end, itv.end)
            else:
                res.append(Interval(itv.start, itv.end))
        return res

