class Solution:
    def minCostII(self, costs):
        if not costs:
            return 0
        for i in range(1, len(costs)):
            for k in range(len(costs[0])):
                costs[i][k] += min(costs[i - 1][:k] + costs[i - 1][k + 1:])
        return min(costs[-1])




class Solution:
    def minCostII(self, costs):
        if not costs:
            return 0

        if len(costs) == 1:
            return min(costs[0])
        N = len(costs[0])
        k_sum_costs = [0] * N

        for cost in costs:
            prev_other_min_sum_costs = [float('inf')] * (N + 1)
            for idx, s_cost in enumerate(k_sum_costs):
                prev_other_min_sum_costs[idx + 1] = min(prev_other_min_sum_costs[idx], s_cost)

            later_other_min_sum_costs = [float('inf')] * (N + 1)
            for idx, s_cost in reversed(list(enumerate(k_sum_costs))):
                later_other_min_sum_costs[idx] = min(s_cost, later_other_min_sum_costs[idx + 1])

            other_min_sum_costs = [min(prev, later) for prev, later in zip(prev_other_min_sum_costs[:-1], later_other_min_sum_costs[1:])]
            for i in range(N):
                k_sum_costs[i] = cost[i] + other_min_sum_costs[i]

        return min(k_sum_costs)
