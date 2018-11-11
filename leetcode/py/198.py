'''
sum_at[-2] = 0
sum_at[-1] = 0
sum_at[0] = max(sum_at[-2] + nums[0], sum_at[-1]) = nums[0]
sum_at[1] = max(sum_at[-1] + nums[1], sum_at[0]) = max(nums[0], nums[1])
sum_at[2] = max(sum_at[0] + nums[2], sum_at[1]) = ..
sum_at[i] = max(sum_at[i - 2] + nums[i], sum_at[i - 1])
'''
class Solution(object):
    def rob(self, nums):
        sum_at_prev, sum_at_pprev = 0, 0

        for num in nums:
            sum_at_prev, sum_at_pprev = max(sum_at_prev, sum_at_pprev + num), sum_at_prev

        return sum_at_prev
