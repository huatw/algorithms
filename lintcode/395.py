# dp[i] = max(
#           values[i] + min(dp[i + 2], dp[i + 3]),
#           values[i] + values[i + 1] + min(dp[i + 3], dp[i + 4])
#         )

class Solution:
    def firstWillWin(self, values):
        if not values:
            return False
        if len(values) < 3:
            return True
        total = sum(values)

        dp = [None] * len(values)
        dp[-1], dp[-2], dp[-3] = values[-1], values[-1] + values[-2], values[-2] + values[-3]

        for i, value in reversed(list(enumerate(values[:-3]))):
            if i + 4 == len(values):
                dp[i] = max(value + min(dp[i + 2], dp[i + 3]), value + values[i + 1] + dp[i + 3])
            else:
                dp[i] = max(value + min(dp[i + 2], dp[i + 3]), value + values[i + 1] + min(dp[i + 3], dp[i + 4]))

        return dp[0] > total - dp[0]