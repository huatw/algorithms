class Solution:
    def longestValidParentheses(self, s):
        start = -1
        stack = []
        res = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif not stack:
                start = i
            else:
                stack.pop()
                if not stack:
                    res = max(res, i - start)
                else:
                    res = max(res, i - stack[-1])
        return res



# DP O(n) O(n)
class Solution:
    def longestValidParentheses(self, s):
        if not s:
            return 0

        dp = [0] * len(s)
        stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif stack:
                idx = stack.pop()
                dp[i] = i - idx + 1

        for i, n in enumerate(dp):
            if i > n:
                dp[i] = n + dp[i - n]

        return max(dp)


# DP O(n) O(n)
class Solution:
    def longestValidParentheses(self, s):
        if not s:
            return 0

        dp = [0] * len(s)
        stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif stack:
                idx = stack.pop()
                dp[i] = i - idx + 1
                if i > dp[i]:
                    dp[i] += dp[i - dp[i]]

        return max(dp)


'''
( ( ) ( ) ( ) )
0 0 2 0 2 0 2 8 single_paren
( ) ( ) ( )
0 2 0 2 0 2
0 2 0 4 0 6 compound_paren
state transform between idx?
len_paren => len(single_paren) => i_right - i_left
             len(compound_paren) => sum([len(single_paren)])
dp: accumulate state of single_paren
'''

'''
( ( ) ( ) )
0 0 2 0 2 6
( ) ( ( ) ) ) ( ) ( ( ) ( )
0 2 0 0 2 4 0 0 2 0 0 2 0 2
( ( ( ) ) ) ( ) ( ( ( ) ) ) ) ( ( ) )
0 0 0 2 4 6 0 2 0 0 0 2 4 6 0 0 0 2 4
              8           14
'''