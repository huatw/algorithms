class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        lo = 1
        for hi, num in enumerate(nums):
            if hi > 0 and num != nums[hi - 1]:
                nums[lo] = num
                lo += 1
        return lo

