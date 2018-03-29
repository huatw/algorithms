class Solution:
    def containsNearbyDuplicate(self, nums, k):
        map = {}

        for i, n in enumerate(nums):
            if n in map and k >= i - map[n]:
                return True
            map[n] = i

        return False

