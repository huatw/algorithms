# O(n) O(n)
class Solution:
    def firstMissingPositive(self, nums):
        nums = set(nums)
        for num in range(1, len(nums) + 2):
            if num not in nums:
                return num




# O(n) O(1)
class Solution:
    def firstMissingPositive(self, nums):
        for i, num in enumerate(nums):
            if not (len(nums) >= num > 0):
                nums[i] = float('inf')
        for num in nums:
            idx = abs(num) - 1
            if idx != float('inf') and nums[idx] > 0:
                nums[idx] = -nums[idx]
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        return len(nums) + 1
