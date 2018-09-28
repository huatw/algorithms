class Solution:
    def majorityElement(self, nums):
        n_map = collections.defaultdict(int)

        for n in nums:
            n_map[n] += 1
            if n_map[n] > len(nums) / 2:
                return n
