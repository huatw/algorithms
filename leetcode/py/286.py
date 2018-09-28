class Solution:
    def missingNumber(self, nums):
        total = int(len(nums) * (len(nums) + 1) / 2)
        return total - sum(nums)