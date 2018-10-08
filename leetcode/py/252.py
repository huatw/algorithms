"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key = lambda itv: itv.start)

        for i, itv in enumerate(intervals[:-1]):
            if itv.end > intervals[i + 1].start:
                return False

        return True
