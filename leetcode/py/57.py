# O(logn)
class Solution:
    def insert(self, intervals, newInterval):

# O(n)
class Solution:
    def insert(self, intervals, new_interval):
        if not intervals:
            return [new_interval]

        res = []
        is_add = False

        for itv in intervals:
            if itv.start > new_interval.end:
                if not is_add:
                    is_add = True
                    res.append(new_interval)
                res.append(itv)
            elif itv.end < new_interval.start:
                res.append(itv)
            else:
                if not is_add:
                    is_add = True
                    res.append(new_interval)
                new_interval.start = min(itv.start, new_interval.start)
                new_interval.end = max(itv.end, new_interval.end)
        if not is_add:
            res.append(new_interval)
        return res


class Solution:
    def insert(self, intervals, new_interval):
        start, end = new_interval.start, new_interval.end
        res = []
        i = 0
        while i < len(intervals):
            if start > intervals[i].end:
                res.append(intervals[i])
            elif end < intervals[i].start:
                break
            else: # overlapping
                start, end = min(start, intervals[i].start), max(end, intervals[i].end)
            i += 1
        return res + [Interval(start, end)] + intervals[i:]
