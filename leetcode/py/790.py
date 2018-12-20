'''
dp[i - 1] = dp[i - 2] + dp[i - 3] + 2 * (dp[i - 4] .. dp[0])
dp[i] = dp[i - 1] + dp[i - 2] + 2*(dp[i - 3] ... dp[0])
      = 2 * dp[i - 1] + dp[i - 3]
'''
class Solution:
    def numTilings(self, N):
        MOD = 10 ** 9 + 7
        dp = [1, 2, 5]

        if N <= 3:
            return dp[N]

        for _ in range(N - 3):
            dp = dp[1], dp[2], (2 * dp[2] + dp[0]) % MOD

        return dp[-1]
