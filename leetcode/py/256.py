class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        costs_red, costs_green, costs_blue = [0], [0], [0]

        for cost in costs:
            pre_costs_red, pre_costs_green, pre_costs_blue = costs_red[-1], costs_green[-1], costs_blue[-1]
            costs_red.append(cost[0] + min(pre_costs_green, pre_costs_blue))
            costs_green.append(cost[1] + min(pre_costs_red, pre_costs_blue))
            costs_blue.append(cost[2] + min(pre_costs_green, pre_costs_red))

        return min(costs_red[-1], costs_green[-1], costs_blue[-1])


class Solution:
    def minCost(self, costs):
        cost_red, cost_green, cost_blue = 0, 0, 0

        for cost in costs:
            cost_red, cost_green, cost_blue = cost[0] + min(cost_green, cost_blue), cost[1] + min(cost_red, cost_blue), cost[2] + min(cost_green, cost_red)

        return min(cost_red, cost_green, cost_blue)