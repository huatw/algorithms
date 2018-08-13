# greedy
class Solution:
    def canJump(self, nums):
        max_distance = 0

        for i, n in enumerate(nums):
            if i > max_distance:
                return False
            max_distance = max(max_distance, i + n)

        return True
