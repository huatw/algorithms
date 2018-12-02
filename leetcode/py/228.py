class Solution:
    def summaryRanges(self, nums):
        res = []

        for num in nums:
            if not res:
                res.append([num])
            else:
                if num == res[-1][-1] + 1:
                    res[-1].append(num)
                else:
                    res.append([num])

        return [str(ns[0]) if ns[0] == ns[-1] else str(ns[0]) + '->' + str(ns[-1]) for ns in res]

class Solution:
    def summaryRanges(self, nums):
        res = []

        for num in nums:
            if res and res[-1][1] + 1 == num:
                res[-1][1] = num
            else:
                res.append([num, num])

        return [str(lo) if lo == hi else str(lo) + '->' + str(hi) for (lo, hi) in res]