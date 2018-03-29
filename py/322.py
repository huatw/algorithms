# DP O(mn)
class Solution(object):
    def coinChange(self, coins, amount):
        res = [float('inf')] * (amount + 1)
        res[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= amount and res[i - coin] + 1 < res[i]:
                    res[i] = res[i - coin] + 1

        return res[-1] if res[-1] != float('inf') else -1
