class MyCalendarTwo:
    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start, end):
        for s, e in self.overlaps:
            if start < e and end > s:
                return False

        for s, e in self.calendar:
            if start < e and end > s:
                self.overlaps.append((max(start, s), min(end, e)))

        self.calendar.append((start, end))
        return True
