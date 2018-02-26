class Solution:
    def topKFrequent(self, nums, k):
        return [k for k, v in collections.Counter(nums).most_common(k)]

