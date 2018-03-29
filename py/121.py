class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        minPrice, maxProf = float('inf'), 0

        for price in prices:
            maxProf = max(maxProf, price - minPrice)
            minPrice = min(minPrice, price)

        return maxProf



