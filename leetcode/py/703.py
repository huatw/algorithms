class KthLargest:
    def __init__(self, k, nums):
        self.hq = []
        self.size = k
        for num in nums:
            if len(self.hq) == self.size:
                heapq.heappushpop(self.hq, num)
            else:
                heapq.heappush(self.hq, num)

    def add(self, val):
        if len(self.hq) == self.size:
            if val > self.hq[0]:
                heapq.heappushpop(self.hq, val)
        else:
            heapq.heappush(self.hq, val)
        return self.hq[0]
