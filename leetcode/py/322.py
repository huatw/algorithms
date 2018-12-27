class Solution:
    def coinChange(self, coins, amount):
        res = [-1] * (amount + 1)
        res[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                if res[i - coin] != -1:
                    if res[i] == -1:
                        res[i] = res[i - coin] + 1
                    else:
                        res[i] = min(res[i], res[i - coin] + 1)
        return res[-1]

class Solution:
    def coinChange(self, coins, amount):
        res = [float('inf')] * (amount + 1)
        res[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                res[i] = min(res[i], res[i - coin] + 1)
        return -1 if res[-1] == float('inf') else res[-1]




import functools
class Solution:
    def coinChange(self, coins, amount):
        @functools.lru_cache(None)
        def dfs(rest_amount):
            if rest_amount == 0:
                return 0

            ns = [dfs(rest_amount - coin) for coin in coins if coin <= rest_amount]
            ns = [n for n in ns if n != -1]
            if not ns:
                return -1
            return 1 + min(ns)

        return dfs(amount)



import functools
class Solution:
    def coinChange(self, coins, amount):
        @functools.lru_cache(None)
        def dfs(rest_amount):
            if rest_amount < 0:
                return float('inf')
            if rest_amount == 0:
                return 0
            return min(dfs(rest_amount - coin) + 1 for coin in coins)

        res = dfs(amount)
        return -1 if res == float('inf') else res
