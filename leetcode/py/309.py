# DP
# thinking in state machine!!!
# free -> hold -> cool -> free
# free cool - free
# free hold - hold
# hold - cool
class Solution(object):
    def maxProfit(self, prices):
        free, cool, hold = 0, -float('inf'), -float('inf')

        for price in prices:
            free, cool, hold = max(free, cool), hold + price, max(free - price, hold)

        return max(free, cool)



