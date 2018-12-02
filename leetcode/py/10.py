'''
s = "aab"
p = "c*a*b"
Output: true
     a a b
   T F F F
c  F F F F
*  T F F F
a  F T F F
*  T T T F
b  F F F T

s = "ab"
p = ".*"
Output: true
    a b c
  T F F F
. F T F F
* T T T T
dp[i][j]
'''

class Solution:
    def isMatch(self, s, p):
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i, chp in enumerate(p):
            if chp == '*':
                dp[i + 1][0] = dp[i - 1][0]

        for i, chp in enumerate(p):
            for j, chs in enumerate(s):
                if chp == '.': # keep previous is match, since . always matches
                    dp[i + 1][j + 1] = dp[i][j]
                elif chp == '*':
                    if p[i - 1] == '.': # match prev ch 0 / 1 / >1
                        dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1] or dp[i + 1][j]
                    else: # match prev ch 0 / 1 / >1
                        dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1] or (dp[i + 1][j] and chs == s[j - 1] == p[i - 1])
                else: # keep previous is match, if chs chp matches
                    dp[i + 1][j + 1] = dp[i][j] and chs == chp

        return dp[-1][-1]

