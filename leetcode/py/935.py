class Solution:
    def knightDialer(self, N):
        MOD = 10 ** 9 + 7
        MOVES = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        dp = [1] * 10
        for _ in range(N - 1):
            next_dp = [0] * 10
            for digit, cnt in enumerate(dp):
                for next_digit in MOVES[digit]:
                    next_dp[next_digit] += cnt
                    next_dp[next_digit] %= MOD
            dp = next_dp
        return sum(dp) % MOD
