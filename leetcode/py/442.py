class Solution:
    def findDuplicates(self, nums):
        res = []

        for num in nums:
            n = abs(num)
            if nums[n - 1] > 0:
                nums[n - 1] = -nums[n - 1]
            else:
                res.append(n)

        return res