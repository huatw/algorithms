# ?
class Solution:
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()

        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])

        return res

# DFS
class Solution:
    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        res = []

        def dfs(acc_nums, rest_nums):
            res.append(acc_nums)
            for i, num in enumerate(rest_nums): #[1, 2, 2, 3]
                if i == 0 or rest_nums[i - 1] != num:
                    dfs(acc_nums + [num], rest_nums[i + 1:])

        dfs([], nums)

        return res


class Solution:
    def subsetsWithDup(self, nums):
        nums = sorted(nums)
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