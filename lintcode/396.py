class Solution:
    def firstWillWin(self, values):
        if not values:
            return False
        N = len(values)
        totals = [0]
        for value in values:
            totals.append(value + totals[-1])

        dp = [[0] * (N + 1) for _ in range(N + 1)]
        visited = [[False] * (N + 1) for _ in range(N + 1)]

        return self.search(1, N, totals, dp, visited) > totals[N] // 2

    def search(self, start, end, totals, dp, visited):
        if not visited[start][end]:
            if start == end:
                visited[start][end] = True
                dp[start][end] = totals[end] - totals[start - 1]
            else:
                max_val = (totals[end] - totals[start - 1]) - min(self.search(start, end - 1, totals, dp, visited), self.search(start + 1, end, totals, dp, visited));
                visited[start][end] = True
                dp[start][end] = max_val
        return dp[start][end]
