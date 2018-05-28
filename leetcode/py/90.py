# DFS
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []

        def dfs(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                if not (i > start and nums[i] == nums[i - 1]):
                    dfs(i + 1, path + [nums[i]])

        dfs(0, [])

        return res




# set
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = {()}

        for n in nums:
            for sub in set(res):
                res.add(sub + (n,))

        return [list(sub) for sub in res]