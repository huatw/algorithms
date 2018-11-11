'''
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

---
  ---

  ---
---
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# O(n)
class Solution:
    def insert(self, intervals, new_interval):
        if not new_interval:
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




# O(logn)
class Solution:
    def insert(self, intervals, newInterval):
