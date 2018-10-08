# DP state transition thinking
# max_profit[i] = max(max_free[i], max_hold[i]) = max_free[i]
# max_free[i] = max(max_hold[i - 1] + stock[i], max_free[i - 1])
# max_hold[i] = max(max_free[i] - stock[i], max_hold[i - 1])

class Solution:
    def maxProfit(self, prices):
        max_free, max_hold = 0, -float('inf')

        for i, price in enumerate(prices):
            max_free = max(max_hold + price, max_free)
            max_hold = max(max_free - price, max_hold)

        return max_free


# more generic thinking
class Solution(object):
    def maxProfit(self, prices):
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



