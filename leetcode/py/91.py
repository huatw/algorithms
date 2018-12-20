'''
26
dp[i] = dp[i - 1] + (dp[i - 2] if 26 >= ch[i - 1:i + 1] >= 10 else 0)
'''
import functools
class Solution:
    def numDecodings(self, s):
        @functools.lru_cache(None)
        def dfs(idx):
            if idx < 0:
                return 1
            val = 0
            if 10 > int(s[idx]) > 0:
                val += dfs(idx - 1)
            if idx > 0 and 26 >= int(s[idx - 1:idx + 1]) >= 10:
                val += dfs(idx - 2)
            return val

        return dfs(len(s) - 1)

class Solution:
    def numDecodings(self, s):
        dp = [1]

        for i, ch in enumerate(s):
            val = 0
            if ch != '0':
                val = dp[-1]
            elif i == 0 or s[i - 1] == '0':
                return 0
            if i > 0 and 26 >= int(s[i - 1:i + 1]) >= 10:
                val += dp[-2]
            dp.append(val)

        return dp[-1]
