'''
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
dp[i] = dp[i - 1] + (dp[i - 2] if 26 >= ch[i - 1:i + 1] >= 1 else 0)
'''
class Solution:
    def numDecodings(self, s):
        dp = [1]

        for i, ch in enumerate(s):
            val = 0
            if ch != '0':
                val = dp[-1]
            elif i == 0 or s[i - 1] == '0':
                return 0
            if i > 0 and 26 >= int(s[i - 1:i + 1]) >= 10:
                val += dp[-2]
            dp.append(val)

        return dp[-1]
