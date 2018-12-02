class UnionFind:
    def __init__(self):
        self.m = {}
        self.size = 0

    def add(self, p):
        self.m[p] = p
        self.size += 1

    def union(self, p1, p2):
        if p2 not in self.m:
            return
        r1, r2 = self.find(p1), self.find(p2)
        if r1 != r2:
            self.size -= 1
            self.m[r1] = r2

    def find(self, p):
        if self.m[p] != p:
            self.m[p] = self.find(self.m[p])
        return self.m[p]

class Solution:
    def numIslands2(self, m, n, positions):
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        uf = UnionFind()
        res = []

        for x, y in positions:
            uf.add((x, y))
            for dx, dy in DIRECTIONS:
                uf.union((x, y), (dx + x, dy + y))
            res.append(uf.size)

        return res
