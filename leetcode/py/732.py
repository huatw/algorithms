import bisect

class MyCalendarThree:
    def __init__(self):
        self.events = []

    def book(self, start, end):
        bisect.insort(self.events, (start, 1))
        bisect.insort_left(self.events, (end, -1))
        res = float('-inf')
        book = 0
        for _, v in self.events:
            book += v
            res = max(res, book)
        return res