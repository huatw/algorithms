class Solution:
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        min_diff = float('inf')
        res = None

        for i, num in enumerate(nums[:-2]):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                total = num + nums[lo] + nums[hi]
                diff = abs(total - target)
                if diff < min_diff:
                    min_diff = diff
                    res = total
                if total < target:
                    lo += 1
                elif total > target:
                    hi -= 1
                else:
                    return res
        return res

