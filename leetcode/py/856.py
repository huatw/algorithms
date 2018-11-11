'''
Input: "(()(()))"
Output: 6
'''
class Solution:
    def scoreOfParentheses(self, S):
        res = 0
        cnt = 0

        for i, ch in enumerate(S):
            if ch == '(':
                cnt += 1
            else:
                cnt -= 1
                if S[i - 1] == '(':
                    res += 2 ** cnt

        return res


class Solution:
    def scoreOfParentheses(self, S):
        res = 0
        stack = [[None, 0]]

        for ch in S:
            if ch == '(':
                stack.append([ch, 0])
            else:
                _, point = stack.pop()
                if point == 0:
                    stack[-1][1] += 1
                else:
                    stack[-1][1] += point * 2

        return stack[-1][1]
