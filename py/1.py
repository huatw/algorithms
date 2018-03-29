class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}

        for idx, n in enumerate(nums):
            if n in map:
                return [map[n], idx]

            map[target-n] = idx
