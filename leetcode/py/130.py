class UnionFind:
    def __init__(self, n):
        self.fathers = [i for i in range(n)]
        self.count = n

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)

        if fx != fy:
            self.fathers[fx] = fy
            self.count -= 1

    def find(self, x):
        if self.fathers[x] == x:
            return x

        self.fathers[x] = self.find(self.fathers[x])
        return self.fathers[x]

class Solution:
    def validTree(self, n, edges):
        uf = UnionFind(n)

        for x, y in edges:
            cnt = uf.count
            uf.union(x, y)
            if uf.count == cnt:
                return False

        return uf.count == 1


