# important DP
# input: prices
# initial state, states: profit1, profit2 <= states: buy1 buy2 price
# output: two profit
class Solution(object):
    def maxProfit(self, prices):
        buy1, buy2, profit1, profit2 = -float('inf'), -float('inf'), 0, 0

        for price in prices:
            profit2 = max(profit2, buy2 + price)
            buy2 = max(buy2, profit1 - price)
            profit1 = max(profit1, buy1 + price)
            buy1 = max(buy1, -price)

        return profit2



