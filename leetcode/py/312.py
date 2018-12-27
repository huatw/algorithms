import functools

class Solution:
    def maxCoins(self, nums):
        @functools.lru_cache(None)
        def dfs(lo, hi):
            if hi - lo <= 1:
                return 0
            return max(nums[lo] * nums[i] * nums[hi] + dfs(lo, i) + dfs(i, hi) for i in range(lo + 1, hi))
        nums = [1] + [n for n in nums if n > 0] + [1]
        return dfs(0, len(nums) - 1)


class Solution:
    def maxCoins(self, nums):
        nums = [1] + [n for n in nums if n > 0] + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]

        def dfs(lo, hi):
            if dp[lo][hi] == 0 and hi - lo > 1:
                dp[lo][hi] = max(nums[lo] * nums[i] * nums[hi] + dfs(lo, i) + dfs(i, hi) for i in range(lo + 1, hi))
            return dp[lo][hi]

        return dfs(0, len(nums) - 1)


class Solution:
    def maxCoins(self, nums):
        nums = [1] + [n for n in nums if n > 0] + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]

        for hi in range(len(nums)):
            for lo in reversed(range(hi - 1)):
                dp[lo][hi] = max(nums[lo] * nums[i] * nums[hi] + dp[lo][i] + dp[i][hi] for i in range(lo + 1, hi))

        return dp[0][-1]
