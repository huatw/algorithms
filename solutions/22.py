class Solution:
    def generateParenthesis(self, n):
        res = []

        def dfs(left_n, right_n, path):
            if left_n == 0:
                res.append(path + ')' * right_n)
                return

            if right_n > left_n:
                dfs(left_n, right_n - 1, path + ')')

            dfs(left_n - 1, right_n, path + '(')


        dfs(n, n, '')

        return res