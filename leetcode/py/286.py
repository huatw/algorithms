class Solution:
    def missingNumber(self, nums):
        N = len(nums)
        total = N * (N + 1) // 2
        return total - sum(nums)
