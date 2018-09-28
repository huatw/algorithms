class Solution:
    def twoSum(self, nums, target):
        map = {}

        for idx, n in enumerate(nums):
            if n in map:
                return [map[n], idx]

            map[target-n] = idx
