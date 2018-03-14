# DFS
class Solution:
    def permuteUnique(self, nums):
        res = []

        nums.sort()

        def dfs(ns, path):
            if not ns:
                res.append(path)
                return

            for i, n in enumerate(ns):
                if not (i > 0 and ns[i] == ns[i - 1]):
                    dfs(ns[:i] + ns[i + 1:], path + [n])

        dfs(nums, [])
        return res


