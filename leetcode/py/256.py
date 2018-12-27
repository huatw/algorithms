class Solution:
    def minCost(self, costs):
        cost_red, cost_green, cost_blue = 0, 0, 0

        for cost in costs:
            cost_red, cost_green, cost_blue = cost[0] + min(cost_green, cost_blue), cost[1] + min(cost_red, cost_blue), cost[2] + min(cost_green, cost_red)

        return min(cost_red, cost_green, cost_blue)