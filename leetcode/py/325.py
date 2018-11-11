'''
[1, -1, 5, -2, 3], k = 3, return 4. # [1, -1, 5, -2]

'''
class Solution:
    def maxSubArrayLen(self, nums, k):
        prev_sum_map = {0: -1}
        total = 0
        res = 0

        for i, num in enumerate(nums):
            total += num
            diff = total - k
            if diff in prev_sum_map:
                res = max(res, i - prev_sum_map[diff])
            if total not in prev_sum_map:
                prev_sum_map[total] = i

        return res

