import functools

class Solution:
    def canIWin(self, max_int, target):
        @functools.lru_cache(None)
        def dfs(nums, total):
            if total + nums[-1] >= target:
                return True
            return any(not dfs(nums[:i] + nums[i + 1:], total + num) \
                for i, num in enumerate(nums))

        if max_int * (1 + max_int) < target * 2:
            return False
        return dfs(tuple(range(1, max_int + 1)), 0)




class Solution:
    def canIWin(self, max_int, target):
        def with_cache(fn):
            cache = {}
            def helper(nums, total):
                if (nums, total) not in cache:
                    cache[(nums, total)] = fn(nums, total)
                return cache[(nums, total)]
            return helper

        @with_cache
        def dfs(nums, total):
            if total + nums[-1] >= target:
                return True
            return any(not dfs(nums[:i] + nums[i + 1:], total + num) \
                for i, num in enumerate(nums))

        if max_int * (1 + max_int) / 2 < target:
            return False

        return dfs(tuple(range(1, max_int + 1)), 0)
