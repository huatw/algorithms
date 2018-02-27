# DP n2 space n
class Solution(object):
    def largestDivisibleSubset(self, nums):
        nums.sort()

        pre, count = [-1] * len(nums), [0] * len(nums)
        maxIdx, maxCount = -1, -1

        for i, num in enumerate(nums):
            for j, n in enumerate(nums[:i]):
                if n*2 > num:
                    break
                if num % n == 0 and count[j] + 1 > count[i]:
                    pre[i], count[i] = j, count[j] + 1

            if count[i] > maxCount:
                maxCount, maxIdx = count[i], i

        res = []
        while maxIdx != -1:
            res.append(nums[maxIdx])
            maxIdx = pre[maxIdx]

        return res




# space n2
def largestDivisibleSubset(self, nums):
    S = {-1: set()}
    for x in sorted(nums):
        S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
    return list(max(S.values(), key=len))
