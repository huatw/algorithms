class UnionFind:
    def __init__(self):
        self.m = {}

    def union(self, n1, n2):
        if n1 not in self.m:
            self.m[n1] = n1
        if n2 not in self.m:
            self.m[n2] = n2
        r1, r2 = self.find(n1), self.find(n2)
        if r1 != r2:
            self.m[r1] = r2
            return True
        return False

    def find(self, n):
        if self.m[n] != n:
            self.m[n] = self.find(self.m[n])
        return self.m[n]


class Solution:
    def findRedundantConnection(self, edges):
        uf = UnionFind()
        for edge in edges:
            if not uf.union(*edge):
                return edge
