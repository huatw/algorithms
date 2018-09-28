class Solution:
    def maxProduct(self, nums):
        max_acc, min_acc = 1, 1
        res = -float('inf')

        for n in nums:
            max_acc, min_acc = max(max_acc * n, min_acc * n, n), min(max_acc * n, min_acc * n, n)
            res = max(res, max_acc, min_acc)

        return res
