class HitCounter:
    def __init__(self):
        self.dq = collections.deque()

    def clean_dq(self, timestamp):
        while self.dq and timestamp - self.dq[0] >= 300:
            self.dq.popleft()

    def hit(self, timestamp):
        self.clean_dq(timestamp)
        self.dq.append(timestamp)

    def getHits(self, timestamp):
        self.clean_dq(timestamp)
        return len(self.dq)

'''
What if the number of hits per second could be very large?
Does your design scale?
'''