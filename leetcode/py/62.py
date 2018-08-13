#DP
class Solution:
    def uniquePaths(self, m, n):
        res = [[0] * (n + 1) for _ in range(m + 1)]
        res[0][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                res[i][j] = res[i][j - 1] + res[i - 1][j]

        return res[-1][-1]
