class Solution:
    def removeDuplicates(self, nums):
        idx, prevN = 0, None

        for i, n in enumerate(nums):
            if n != prevN:
                if i != idx:
                    nums[i], nums[idx] = nums[idx], n
                idx += 1
            prevN = n

        return idx




class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if i != idx:
                    nums[idx] = nums[i]
                idx += 1

        return idx



