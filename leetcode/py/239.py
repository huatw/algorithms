class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        dq = collections.deque()

        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)
            while i - dq[0] >= k:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
