class Solution:
    def summaryRanges(self, nums):
        res = []

        for num in nums:
            if res and res[-1][1] + 1 == num:
                res[-1][1] = num
            else:
                res.append([num, num])

        return [str(lo) if lo == hi else str(lo) + '->' + str(hi) for (lo, hi) in res]