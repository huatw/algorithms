# DP
class Solution(object):
    def combinationSum3(self, k, n):
        res = [[] for _ in range(n + 1)] # sum, cnt
        res[0].append([[], 0, 0])

        for v in range(1, 10):
            for i in range(n, v - 1, -1):
                for arr, vSum, cnt in res[i - v]:
                    if cnt < k and vSum + v <= n:
                        res[i].append([arr + [v], vSum + v, cnt + 1])

        return [arr for arr, _, __ in filter(lambda r: r[1] == n and r[2] == k, res[-1])]



# DFS
class Solution(object):
    def combinationSum3(self, k, n):
        res = []

        def dfs(v, remainK, remainN, paths):
            if remainK < 0 or remainN < 0:
                return
            if remainK == 0 and remainN == 0:
                res.append(paths)

            for val in range(v, 10):
                dfs(val + 1, remainK-1, remainN-val, paths + [val])

        dfs(1, k, n, [])

        return res



