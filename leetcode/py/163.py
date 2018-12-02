'''
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
'''
class Solution:
    def findMissingRanges(self, nums, lower, upper):
        idx = 0
        num_ranges = []

        while idx < len(nums):
            start = nums[idx]
            while idx + 1 < len(nums) and nums[idx + 1] == nums[idx] + 1:
                idx += 1
            num_ranges.append((start, nums[idx]))
            idx += 1

        num_ranges = [(None, lower - 1)] + num_ranges + [(upper + 1, None)]
        res = []
        for (_, end), (start, _) in zip(num_ranges, num_ranges[1:]):
            if start - end == 2:
                res.append(str(end + 1))
            elif start - end > 2:
                res.append(str(end + 1) + '->' + str(start - 1))
        return res
