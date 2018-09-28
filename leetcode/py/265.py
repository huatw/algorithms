class Solution:
    def minCostII(self, costs):
        if not costs:
            return 0

        k_sum_costs = [0] * len(costs[0])

        for cost in costs:
            prev_other_min_sum_costs = [float('inf')]
            for s_cost in k_sum_costs:
                prev_other_min_sum_costs.append(min(prev_other_min_sum_costs[-1], s_cost))

            later_other_min_sum_costs = [float('inf')] * (len(costs[0]) + 1)
            for idx, s_cost in reversed(list(enumerate(k_sum_costs))):
                later_other_min_sum_costs[idx] = min(s_cost, later_other_min_sum_costs[idx + 1])

            other_min_sum_costs = [min(prev, later) for (prev, later) in zip(prev_other_min_sum_costs[:-1], later_other_min_sum_costs[1:])]

            for i in range(len(costs[0])):
                k_sum_costs[i] = cost[i] + other_min_sum_costs[i]

        return min(k_sum_costs)



# TLE
class Solution:
    def minCostII(self, costs):
        if not costs:
            return 0

        k_sum_costs = [0] * len(costs[0])

        for cost in costs:
            prev_k_sum_costs = [*k_sum_costs]

            for i in range(len(costs[0])):
                # this will TLE
                k_sum_costs[i] = cost[i] + min(*prev_k_sum_costs[:i], *prev_k_sum_costs[i + 1:])

        return min(k_sum_costs)