class Solution:
    def twoSum(self, nums, target):
        map = {}

        for idx, n in enumerate(nums):
            if n in map:
                return [map[n], idx]

            map[target-n] = idx

class Solution:
    def twoSum(self, nums, target):
        num_idx_map = {}

        for i, num in enumerate(nums):
            if target - num in num_idx_map:
                return [num_idx_map[target - num], i]
            num_idx_map[num] = i

