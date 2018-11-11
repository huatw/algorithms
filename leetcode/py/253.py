"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# O(nlogn)
import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        intervals = sorted(intervals, key = lambda m: m.start)
        hq = []
        for itv in intervals:
            if hq and hq[0] < itv.start:
                heapq.heappop(hq)
            heapq.heappush(hq, itv.end)

        return len(hq)