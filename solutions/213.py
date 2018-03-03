class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0

        if len(nums) < 4:
            return max(nums)

        pSum, ppSum = 0, 0

        for n in nums[:-1]:
            pSum, ppSum = max(ppSum + n, pSum), pSum

        res = pSum

        pSum, ppSum = 0, 0
        for n in nums[1:]:
            pSum, ppSum = max(ppSum + n, pSum), pSum

        return max(res, pSum)



