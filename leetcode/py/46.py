# Iter
class Solution:
    def permute(self, nums):
        res = []
        stack = [([], nums)]
        while stack:
            acc, rest_ns = stack.pop()
            if not rest_ns:
                res.append(acc)
                continue
            for i, n in enumerate(rest_ns):
                stack.append((acc + [n], rest_ns[:i] + rest_ns[i + 1:]))
        return res


# DFS O(n2) O(n2)
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