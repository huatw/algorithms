class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0

        res = 0
        cnt = 0
        for prev_n, next_n in zip(nums, nums[1:]):
            if prev_n < next_n:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 0
        return max(res, cnt) + 1
