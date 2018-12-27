class Solution:
    def wiggleSort(self, nums):
        for i in range(len(nums) - 1):
            should_inc = i % 2 == 0
            if (should_inc and nums[i] > nums[i + 1]) or (not should_inc and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
