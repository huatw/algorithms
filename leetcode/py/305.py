# Union Find
# https://www.lintcode.com/problem/number-of-islands-ii/description
# https://github.com/awangdev/LintCode/blob/master/Java/Number%20of%20Islands%20II.java

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class UnionFind:
    def __init__(self, size):
        self.count = 0
        self.father = [i for i in range(size)]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.count -= 1

    def find(self, x):
        if self.father[x] == x:
            return x

        self.father[x] = self.find(self.father[x])

        return self.father[x]

class Solution:
    def numIslands2(self, n, m, operators):
        ret = []
        dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        grid = [[0] * m for _ in range(n)]

        uf = UnionFind(m * n)

        for op in operators:
            x, y = op.x, op.y
            if grid[x][y] == 1:
                ret.append(uf.count)
                continue

            grid[x][y] = 1
            uf.count += 1

            for (dx, dy) in dxy:
                m_x, m_y = x + dx, y + dy
                if n > m_x >= 0 and m > m_y >= 0 and grid[m_x][m_y] == 1:
                    uf.union(x * m + y, m_x * m + m_y)
            ret.append(uf.count)

        return ret
