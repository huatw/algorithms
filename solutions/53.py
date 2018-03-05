class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 0

        res, val = nums[0], nums[0]

        for n in nums[1:]:
            if val < 0:
                val = n
            else:
                val += n
            res = max(res, val)

        return res



