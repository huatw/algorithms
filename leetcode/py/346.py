class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.dq = collections.deque()
        self.total = 0

    def next(self, val):
        if self.size == len(self.dq):
            self.total -= self.dq.popleft()
        self.dq.append(val)
        self.total += val
        return self.total / len(self.dq)
