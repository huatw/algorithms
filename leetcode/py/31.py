# https://leetcode.com/problems/next-permutation/solution/
'''
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2
        # find first dec val
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # exchange position
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # reverse from i + 1
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1
