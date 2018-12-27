class Solution:
    def change(self, amount, coins):
        res = [0] * (amount + 1)
        res[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                res[i] += res[i - coin]

        return res[-1]


# TLE
import functools
class Solution:
    def change(self, amount, coins):
        @functools.lru_cache(None)
        def dfs(idx, rest_amount):
            if rest_amount == 0:
                return 1
            if rest_amount < 0 or idx == len(coins):
                return 0
            return dfs(idx + 1, rest_amount) + dfs(idx, rest_amount - coins[idx])

        return dfs(0, amount)
