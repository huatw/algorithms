class Solution:
    def missingNumber(self, nums):
        N = len(nums)

        total = N * (N + 1) // 2

        return total - sum(nums)


class Solution:
    def missingNumber(self, nums):
        res = len(nums)

        for i, num in enumerate(nums):
            res ^= i
            res ^= num

        return res