# DP 01backpack O(mnlen(strs))
class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n+1) for _ in range(m+1)]

        for s in strs:
            ones, zeros = s.count('1'), s.count('0')

            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)

        return dp[m][n]

