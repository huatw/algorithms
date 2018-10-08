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
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda itv: itv.start)

        hq = []
        for itv in intervals:
            if hq and hq[0] <= itv.start:
                heapq.heapreplace(hq, itv.end)
            else:
                heapq.heappush(hq, itv.end)

        return len(hq)