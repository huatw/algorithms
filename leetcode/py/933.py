import collections

class RecentCounter:
    def __init__(self):
        self.dq = collections.deque()

    def ping(self, t):
        self.dq.append(t)
        while t - self.dq[0] > 3000:
            self.dq.popleft()
        return len(self.dq)