'''
+++
++-
+--
---
'''
# nlogn
class Solution:
    def maximumProduct(self, nums):
        nums = sorted(nums, reverse = True)

        ppp = nums[0] * nums[1] * nums[2]
        pnn = nums[0] * nums[-2] * nums[-1]
        return max(ppp, pnn)


class Solution:
    def maximumProduct(self, nums):
        max_three = [-float('inf')] * 3
        min_two = [float('inf')] * 2

        for num in nums:
            max_three = sorted(max_three + [num], reverse = True)[:3]
            min_two = sorted(min_two + [num])[:2]

        return max(max_three[0] * max_three[1] * max_three[2], max_three[0] * min_two[0] * min_two[1])