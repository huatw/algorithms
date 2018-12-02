class Solution:
    def threeSumSmaller(self, nums, target):
        nums = sorted(nums)
        res = 0

        for i, num in enumerate(nums[:-2]):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                total = num + nums[lo] + nums[hi]
                if total >= target:
                    hi -= 1
                else:
                    res += hi - lo
                    lo += 1

        return res