def with_cache(fn):
    cache = {}
    def wrapper(lo, hi):
        if (lo, hi) not in cache:
            cache[(lo, hi)] = fn(lo, hi)
        return cache[(lo, hi)]
    return wrapper

class Solution:
    def maxCoins(self, nums):
        @with_cache
        def dfs(lo, hi):
            if hi - lo <= 1:
                return 0
            return max(nums[lo] * nums[i] * nums[hi] + dfs(lo, i) + dfs(i, hi) for i in range(lo + 1, hi))
        nums = [1] + nums + [1]
        return dfs(0, len(nums) - 1)

