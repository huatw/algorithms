class Solution:
    def distinctSubseqII(self, S):
        dp = [1]
        last = {}
        for i, ch in enumerate(S):
            dp.append(dp[-1] * 2)
            if ch in last:
                dp[-1] -= dp[last[ch]]
            last[ch] = i

        return (dp[-1] - 1) % (10 ** 9 + 7)


class Solution:
    def distinctSubseqII(self, S):
        MOD = 10 ** 9 + 7
        dp = [[0] * 26 for _ in range(len(S) + 1)]
        res = 0
        for i in range(len(S)):
            for l in range(i + 1, 0, -1):
                dp[l][ord(S[i]) - ord('a')] = sum(dp[l - 1])
            dp[1][ord(S[i]) - ord('a')] = 1

        return sum(dp[i][j] for i in range(1, len(dp)) for j in range(26)) % MOD


class Solution:
    def distinctSubseqII(self, S):
        dp = [0] * 26
        MOD = 10 ** 9 + 7
        for ch in S:
            dp[ord(ch) - ord('a')] = sum(dp) + 1
        return sum(dp) % MOD

# 强行过...
import functools
class Solution:
    def distinctSubseqII(self, S):
        M = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(idx):
            seen = set()
            total = 0
            for i in range(idx, len(S)):
                if S[i] not in seen:
                    seen.add(S[i])
                    total += 1 + dfs(i + 1)
                if len(seen) == 26:
                    break
            return total

        return dfs(0) % M