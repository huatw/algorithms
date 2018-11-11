import collections

class MovingAverage:

    def __init__(self, size):
        self.size = size
        self.q = collections.deque([], size)
        self.total = 0

    def next(self, val):
        if len(self.q) == self.size:
            self.total -= self.q[0]
        self.q.append(val)
        self.total += val
        return self.total / len(self.q)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)