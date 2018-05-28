class Solution:
    def subsets(self, nums):
        res = [[]]

        for n in nums:
            res += [sub + [n] for sub in res]

        return res
