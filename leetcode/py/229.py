class Solution:
    def majorityElement(self, nums):
        n_map = collections.defaultdict(int)

        for n in nums:
            n_map[n] += 1

        return [k for k, v in n_map.items() if v > len(nums) / 3]
