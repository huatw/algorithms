#DP
class Solution:
    def uniquePaths(self, m, n):
        res = [[0 for _ in range(m)] for _ in range(n)]

        for x, row in enumerate(res):
            for y, acc in enumerate(row):
                if x == 0 and y == 0:
                    res[x][y] = 1
                elif x == 0:
                    res[x][y] = res[x][y - 1]
                elif y == 0:
                    res[x][y] = res[x - 1][y]
                else:
                    res[x][y] = res[x][y - 1] + res[x - 1][y]

        return res[-1][-1]
