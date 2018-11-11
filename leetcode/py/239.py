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




class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        deq = collections.deque() # max len == k

        for i, num in enumerate(nums):
            # pop out smaller ones in deque
            while deq and nums[deq[-1]] < num:
                deq.pop()
            deq.append(i)

            # control the head of deque and deque max length == k
            if deq[0] == i - k:
                deq.popleft()

            # append every time when i > k - 1
            if i >= k - 1:
                res.append(nums[deq[0]])

        return res