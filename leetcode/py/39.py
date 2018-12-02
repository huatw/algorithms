class Solution:
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        res = []

        def dfs(idx, total, path):
            if total > target:
                return
            if total == target:
                res.append([*path])
                return
            for i in range(idx, len(candidates)):
                path.append(candidates[i])
                dfs(i, total + candidates[i], path)
                path.pop()

        dfs(0, 0, [])
        return res


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


