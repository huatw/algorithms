# state transition: free hold cool
# free -> hold/free
# hold -> hold/free
# cool -> free
# free[i] = max(free[i - 1], cool[i - 1]) # before cool
# hold[i] = max(hold[i - 1], free[i - 1] - prices[i]) # before free
# cool[i] = hold[i - 1] + prices[i] # before hold
class Solution:
    def maxProfit(self, prices):
        free, hold, cool = 0, -float('inf'), -float('inf')

        for price in prices:
            free, cool, hold = max(free, cool), hold + price, max(hold, free - price)

        return max(free, cool)



# DP
# thinking in state machine!!!
# free -> hold -> cool -> free
# free cool - free
# free hold - hold
# hold - cool
class Solution:
    def maxProfit(self, prices):
        free, cool, hold = 0, -float('inf'), -float('inf')

        for price in prices:
            free, cool, hold = max(free, cool), hold + price, max(free - price, hold)

        return max(free, cool)



