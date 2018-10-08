# buy1[i] = min(buy1[i - 1], prices[i])
# sell1[i] = max(sell1[i - 1], prices[i] - buy1[i - 1])
# buy2[i] = max(buy2[i - 1], sell1[i] - prices[i]) # notice buy after sell
# sell2[i] = max(sell2[i - 1], buy2[i - 1] + prices[i])
# flat state, change order
class Solution:
    def maxProfit(self, prices):
        buy1, sell1, buy2, sell2 = float('inf'), 0, -float('inf'), 0

        for price in prices:
            sell2 = max(sell2, buy2 + price) # one one depends on sell2
            sell1 = max(sell1, price - buy1) # sell1 sell2 interchangable
            buy2 = max(buy2, sell1 - price)  # buy1 buy2 interchangable
            buy1 = min(buy1, price)

        return sell2


# important DP
# input: prices
# initial state, states: profit1, profit2 <= states: buy1 buy2 price
# output: two profit
class Solution:
    def maxProfit(self, prices):
        buy1, buy2, profit1, profit2 = -float('inf'), -float('inf'), 0, 0

        for price in prices:
            profit2 = max(profit2, buy2 + price)
            buy2 = max(buy2, profit1 - price)
            profit1 = max(profit1, buy1 + price)
            buy1 = max(buy1, -price)

        return profit2



