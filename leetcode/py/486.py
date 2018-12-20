class Solution:
    def PredictTheWinner(self, nums):
        def with_cache(fn):
            cache = {}
            def wrapper(start, end):
                if (start, end) not in cache:
                    cache[start, end] = fn(start, end)
                return cache[start, end]
            return wrapper

        @with_cache
        def dfs(start, end):
            if start == end:
                return nums[start], 0
            second1, first1 = dfs(start + 1, end)
            first1 += nums[start]
            second2, first2 = dfs(start, end - 1)
            first2 += nums[end]

            return (first1, second1) if first1 - second1 > first2 - second2 else (first2, second2)

        first, second = dfs(0, len(nums) - 1)
        return first >= second




class Solution:
    def PredictTheWinner(self, nums):
        dp = [0] * len(nums)
        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[-1] >= 0
