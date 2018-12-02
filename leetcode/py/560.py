'''
k = 10
[3, 5, 2, 1, 2, 5]
 3  8  10 11 13 18
'''
class Solution:
    def subarraySum(self, nums, k):
        total_cnt_map = collections.defaultdict(int, {0: 1})
        total = 0
        res = 0

        for num in nums:
            total += num
            res += total_cnt_map[total - k]
            total_cnt_map[total] += 1
        return res
