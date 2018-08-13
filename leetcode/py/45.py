# greedy

class Solution:
    def jump(self, nums):
        idx = 0
        next_idx = 0
        steps = 0

        for i, num in enumerate(nums):
            if idx + 1 >= len(nums):
                return steps

            next_idx = max(next_idx, i + num)

            if i == idx:
                steps += 1
                idx = next_idx
