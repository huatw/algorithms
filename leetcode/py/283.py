class Solution:
    def moveZeroes(self, nums):
        zeroIdx = 0
        for i, n in enumerate(nums):
            if n != 0:
                if zeroIdx != i:
                    nums[zeroIdx], nums[i] = nums[i], nums[zeroIdx]
                zeroIdx += 1



