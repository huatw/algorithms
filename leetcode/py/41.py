class Solution:
    def firstMissingPositive(self, nums):
        ns = [n if len(nums) >= n > 0 else float('inf') for n in nums]

        for n in ns:
            m = abs(n)
            if m != float('inf') and ns[m - 1] > 0:
                ns[m - 1] = -ns[m - 1]

        for i, n in enumerate(ns):
            if n > 0:
                return i + 1

        return len(nums) + 1