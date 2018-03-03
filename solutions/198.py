class Solution(object):
    def rob(self, nums):
        pSum, ppSum = 0, 0

        for n in nums:
            pSum, ppSum = max(n + ppSum, pSum), pSum

        return pSum



