# DFS
class Solution:
    def permute(self, nums):
        res = []

        def dfs(ns, path):
            if not ns:
                res.append(path)
                return

            for i, n in enumerate(ns):
                dfs(ns[:i] + ns[i + 1:], path + [n])

        dfs(nums, [])
        return res



class Solution:
    def permute(self, nums):
        return map(list, itertools.permutations(nums))