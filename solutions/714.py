class Solution(object):
    def maxProfit(self, prices, fee):
        if not prices or len(prices) < 2:
            return 0

        buy = -prices[0]
        sell = 0

        for price in prices:
            buy, sell = max(buy, sell - price), max(sell, buy + price - fee)

        return sell



