class Solution:
    def removeElement(self, nums, val):
        lo = 0
        for hi, num in enumerate(nums):
            if num != val:
                nums[lo] = num
                lo += 1
        return lo
