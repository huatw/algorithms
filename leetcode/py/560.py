class Solution:
    def subarraySum(self, nums, k):
        cur_sum = 0
        cnt_map = collections.defaultdict(int)
        cnt_map[0] = 1
        res = 0
        for num in nums:
            cur_sum += num
            res += cnt_map[cur_sum - k]
            cnt_map[cur_sum] += 1
        return res
