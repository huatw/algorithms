# MLE
class Solution(object):
    def maxProfit(self, k, prices):
        buys = [-float('inf')] * (k + 1)
        sells = [0] * (k + 1)

        buy1, buy2 = -float('inf'), -float('inf')
        sell1, sell2 = 0, 0

        for price in prices:
            for i in range(k, 0, -1):
                sells[i] = max(sells[i], buys[i] + price)
                buys[i] = max(buys[i], sells[i-1] - price)

        return sells[-1]





# MLE
class Solution(object):
    def maxProfit(self, k, prices):
        if k >= len(prices) // 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)

        buys = [-float('inf')] * (k + 1)
        sells = [0] * (k + 1)

        buy1, buy2 = -float('inf'), -float('inf')
        sell1, sell2 = 0, 0

        for price in prices:
            for i in range(k, 0, -1):
                sells[i] = max(sells[i], buys[i] + price)
                buys[i] = max(buys[i], sells[i-1] - price)

        return sells[-1]
