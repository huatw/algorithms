"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key = lambda itv: itv.start)

        for prev_itv, next_itv in zip(intervals, intervals[1:]):
            if prev_itv.end > next_itv.start:
                return False

        return True