class Solution:
    def triangleNumber(self, nums):
        nums = sorted(nums, reverse = True)
        res = 0
        for i, num in enumerate(nums[:-2]):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                if num < nums[lo] + nums[hi]:
                    res += hi - lo
                    lo += 1
                else:
                    hi -= 1

        return res
