class KthLargest:
    def __init__(self, k, nums):
        self.hq = nums
        self.size = k
        heapq.heapify(self.hq)
        while len(self.hq) > self.size:
            heapq.heappop(self.hq)

    def add(self, val):
        if len(self.hq) < self.size:
            heapq.heappush(self.hq, val)
        elif self.hq[0] < val:
            heapq.heapreplace(self.hq, val)

        return self.hq[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)