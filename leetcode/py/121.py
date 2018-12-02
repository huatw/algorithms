# brute force, two pointer double loop O(n2)
# max_profit[i] = max(max_profit[i - 1], price[i] - min_price[i - 1])
class Solution:
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit
