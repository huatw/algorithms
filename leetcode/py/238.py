# O(n) O(1)
class Solution:
    def productExceptSelf(self, nums):
        res = []

        p = 1
        for num in nums:
            res.append(p)
            p *= num

        p = 1
        for i, num in reversed(list(enumerate(nums))):
            res[i] *= p
            p *= num

        return res