import functools

class Solution:
    def cheapestJump(self, nums, k):
        @functools.lru_cache(None)
        def dfs(i):
            if nums[i - 1] == -1:
                return float('inf'), []

            if i == len(nums):
                return nums[i - 1], [i]

            cost, path = min(map(dfs, range(i + 1, min(i + k, len(nums)) + 1)))

            return nums[i - 1] + cost, [] if cost == float('inf') else [i] + path

        return dfs(1)[1]


class Solution:
    def cheapestJump(self, nums, k):
        if not nums or nums[0] == -1:
            return []

        dp = [(float('inf'), []) for _ in nums]
        dp[0] = (nums[0], [1])

        for j in range(1, len(nums)):
            if nums[j] == -1:
                continue
            dp[j] = min((dp[i][0] + nums[j], dp[i][1] + [j + 1]) for i in range(max(0, j - k), j))

        return dp[-1][1] if dp[-1][0] != float('inf') else []
