class Solution(object):
    def numDecodings(self, s):
        one = collections.defaultdict(
            int,
            {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '*': 9}
        )
        two = collections.defaultdict(
            int,
            {'10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1, '16': 1, '17': 1, '18': 1, '19': 1, '20': 1, '21': 1, '22': 1, '23': 1, '24': 1, '25': 1, '26': 1, '*0': 2, '*1': 2, '*2': 2, '*3': 2, '*4': 2, '*5': 2, '*6': 2, '*7': 1, '*8': 1, '*9': 1, '1*': 9, '2*': 6, '**': 15}
        )

        dp = 1, one[s[:1]]

        for i in range(1, len(s)):
            if dp[1] == 0:
                return 0
            dp = dp[1], (one[s[i]] * dp[1] + two[s[i-1: i+1]] * dp[0]) % 1000000007

        return dp[-1]

