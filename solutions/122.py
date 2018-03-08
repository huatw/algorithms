# more generic thinking
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        buy, sell = -prices[0], 0

        for price in prices:
            buy, sell = max(buy, sell - price), max(sell, buy + price)

        return sell




class Solution(object):
    def maxProfit(self, prices):
        res = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]

        return res




class Solution(object):
    def maxProfit(self, prices):
        return sum([prices[i] - prices[i-1] if prices[i] > prices[i-1] else 0 for i in range(1, len(prices))])



