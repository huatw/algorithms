# DP
'''
    a b c target
  0 1 2 3
a 1 0 1 2
d 2 1 2 3
c 3 1 2 2
'''
class Solution:
    def minDistance(self, word1, word2):
        M, N = len(word1), len(word2)

        dp = [[0] * (N + 1) for i in range(M + 1)]
        dp[0] = [i for i in range(N + 1)]
        for i in range(M + 1):
            dp[i][0] = i

        for i in range(M):
            for j in range(N):
                cost = 0 if word1[i] == word2[j] else 1
                dp[i + 1][j + 1] = min(dp[i + 1][j] + 1, dp[i][j + 1] + 1, dp[i][j] + cost)

        return dp[-1][-1]
