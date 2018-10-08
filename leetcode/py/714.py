# state transition
# how many state?
# 2: hold / free
# hold ->(fee) hold / free
# free ->      hold / free
# hold[i] = max(hold[i - 1], free[i] - prices[i])          # depend on updated free (2)
# free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)# depend on old hold     (1)
class Solution:
    def maxProfit(self, prices, fee):
        hold, free = -float('inf'), 0

        for price in prices:
            free = max(free, hold + price - fee)
            hold = max(hold, free - price)

        return free





#DP
# state machine
# hold <-> free
class Solution:
    def maxProfit(self, prices, fee):
        if not prices or len(prices) < 2:
            return 0

        buy = -prices[0]
        sell = 0

        for price in prices:
            buy, sell = max(buy, sell - price), max(sell, buy + price - fee)

        return sell



