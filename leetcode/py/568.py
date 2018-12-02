class Solution:
    def maxVacationDays(self, flights, days):
        N, K = len(days), len(days[0])
        get_next_cities = lambda city: [city] + [next_city for next_city, has_flight in enumerate(flights[city]) if has_flight == 1]
        cache = [[None] * K for _ in range(N)]

        def dfs(city, n_week):
            if n_week == K:
                return 0
            if cache[city][n_week] == None:
                next_cities = get_next_cities(city)
                cache[city][n_week] = days[city][n_week] + max(dfs(next_city, n_week + 1) for next_city in next_cities)
            return cache[city][n_week]

        other_cities = get_next_cities(0)
        res = dfs(0, 0)
        return max(dfs(city, 0) for city in other_cities)


'''
Input:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[7,0,0],[0,7,0],[0,0,7]]
'''
class Solution:
    def maxVacationDays(self, flights, days):
        N, K = len(days), len(days[0])
        get_next_cities = lambda city: [city] + [next_city for next_city, has_flight in enumerate(flights[city]) if has_flight == 1]
        dp = [[None] * K for _ in range(N)]

        for n_day in reversed(range(K)):
            for n_city in range(N):
                dp[n_city][n_day] = days[n_city][n_day]
                next_cities = get_next_cities(n_city)
                if n_day != K - 1:
                    dp[n_city][n_day] += max(dp[next_city][n_day + 1] for next_city in next_cities)

        return max(dp[city][0] for city in get_next_cities(0))
