class Solution:
    def totalNQueens(self, n):
        res = 0
        cols = [False] * n
        d1 = [False] * 2 * n # \ direction
        d2 = [False] * 2 * n # / direction

        def dfs(row):
            nonlocal res
            if row == n:
                res += 1
                return
            for col in range(n):
                id1, id2 = col - row + n, col + row
                if cols[col] or d1[id1] or d2[id2]:
                    continue
                cols[col], d1[id1], d2[id2] = True, True, True
                dfs(row + 1)
                cols[col], d1[id1], d2[id2] = False, False, False

        dfs(0)

        return res