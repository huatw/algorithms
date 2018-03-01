# dp backpack
class Solution(object):
    def change(self, amount, coins):
        res = [0] * (amount + 1)
        res[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                res[i] += res[i - coin]

        return res[-1]