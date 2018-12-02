# dfs backtracking
class Solution:
    def generateParenthesis(self, n):
        res = []

        def dfs(left_n, right_n, acc):
            if not right_n:
                res.append(''.join(acc))
                return
            if left_n > 0:
                acc.append('(')
                dfs(left_n - 1, right_n, acc)
                acc.pop()
            if right_n > left_n:
                acc.append(')')
                dfs(left_n, right_n - 1, acc)
                acc.pop()

        dfs(n, n, [])
        return res



# dfs
class Solution:
    def generateParenthesis(self, n):
        res = []

        def dfs(left_n, right_n, acc):
            if left_n == 0 and right_n == 0:
                res.append(acc)
                return
            if left_n < right_n:
                dfs(left_n, right_n - 1, acc + ')')
            if left_n:
                dfs(left_n - 1, right_n, acc + '(')

        if n:
            dfs(n, n, '')

        return res