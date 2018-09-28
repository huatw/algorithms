class Solution:
    def productExceptSelf(self, nums):
        res = []
        p = 1
        for n in nums:
            res.append(p)
            p *= n

        p = 1
        for i, n in reversed(list(enumerate(nums))):
            res[i] *= p
            p *= n

        return res
