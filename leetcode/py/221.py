class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for _ in range(M)]

        res = 0
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    if i > 0 and j > 0:
                         dp[i][j] += min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
                    res = max(res, dp[i][j])

        return res ** 2
