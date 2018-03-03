# DP
class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()

        dp = [[[]]]

        for i in range(1, target + 1):
            dp.append([])
            for number in candidates:
                if number > i:
                    break
                for L in dp[i - number]:
                    if not L or number >= L[-1]:
                        dp[i].append(L + [number])

        return dp[target]


