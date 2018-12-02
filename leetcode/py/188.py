# buy1[i] = max(buy1[i - 1], -prices[i])
# sell1[i] = max(sell1[i - 1], prices[i] + buy1[i - 1])
# buy2[i] = max(buy2[i - 1], sell1[i] - prices[i]) # notice buy after sell
# sell2[i] = max(sell2[i - 1], buy2[i - 1] + prices[i])
# buy3[i] = max(buy3[i - 1], sell2[i] - prices[i]) # notice buy after sell
# sell3[i] = max(sell3[i - 1], buy3[i - 1] + prices[i])

# sell(n) = max(sell(n), buy(n) + price)
# ...
# sell2 = max(sell2, buy2 + price)
# sell1 = max(sell1, price + buy1)
# buy(n) = max(buy(n), sell(n-1) - price)
# buy2 = max(buy2, sell1 - price)
# buy1 = min(buy1, prices)

class Solution:
    def maxProfit(self, k, prices):
        if k < 1:
            return 0
        if 2 * k >= len(prices):
            return sum(i - j for i, j in zip(prices[1:], prices) if i - j > 0)

        sells, buys = [0] * k, [-float('inf')] * k

        for price in prices:
            for i, sell in enumerate(sells):
                sells[i] = max(sell, buys[i] + price)
            for i, buy in enumerate(buys):
                buys[i] = max(buy, (0 if i == 0 else sells[i - 1]) - price)

        return max(sells[-1], buys[-1])









# MLE
class Solution:
    def maxProfit(self, k, prices):
        buys = [-float('inf')] * (k + 1)
        sells = [0] * (k + 1)

        for price in prices:
            for i in range(k, 0, -1):
                sells[i] = max(sells[i], buys[i] + price)
                buys[i] = max(buys[i], sells[i-1] - price)

        return sells[-1]





class Solution:
    def maxProfit(self, k, prices):
        if k >= len(prices) // 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)

        buys = [-float('inf')] * (k + 1)
        sells = [0] * (k + 1)

        for price in prices:
            for i in range(k, 0, -1):
                sells[i] = max(sells[i], buys[i] + price)
                buys[i] = max(buys[i], sells[i-1] - price)

        return sells[-1]
