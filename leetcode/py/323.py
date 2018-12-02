class UnionFind:
    def __init__(self, size):
        self.size = size
        self.m = {i: i for i in range(size)}

    def union(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)
        if r1 != r2:
            self.size -= 1
            self.m[r1] = r2

    def find(self, n):
        if self.m[n] != n:
            self.m[n] = self.find(self.m[n])
        return self.m[n]

class Solution:
    def countComponents(self, n, edges):
        uf = UnionFind(n)

        for n1, n2 in edges:
            uf.union(n1, n2)

        return uf.size