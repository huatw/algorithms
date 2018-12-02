class KthLargest:
    def __init__(self, k, nums):
        self.nums = []
        self.size = k
        for val in nums:
            self.add(val)

    def add(self, val):
        if len(self.nums) == self.size:
            heapq.heappushpop(self.nums, val)
        else:
            heapq.heappush(self.nums, val)
        return self.nums[0]
