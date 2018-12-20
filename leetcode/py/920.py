from functools import lru_cache

class Solution:
    def numMusicPlaylists(self, N, L, K):
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return int(j == 0)
            res = dp(i - 1, j - 1) * (N - j + 1)
            res += dp(i - 1, j) * max(j - K, 0)
            return res % MOD

        return dp(L, N)