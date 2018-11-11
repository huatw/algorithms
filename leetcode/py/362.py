import collections
class HitCounter:
    def __init__(self):
        self.dq = collections.deque()

    def hit(self, timestamp):
        self.dq.append(timestamp)

    def getHits(self, timestamp):
        while len(self.dq) and timestamp - self.dq[0] >= 300:
            self.dq.popleft()
        return len(self.dq)

'''
What if the number of hits per second could be very large?
Does your design scale?
'''