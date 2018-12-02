class UnionFind:
    def __init__(self):
        self.m = {}
    def add(self, n1, n2):
        if n1 in self.m:
            self.m[n2] = n1
        elif n2 in self.m:
            self.m[n1] = n2
        else:
            self.m[n1] = n2
            self.m[n2] = n2
        return True
    def add_union(self, n1, n2):
        if n1 in self.m and n2 in self.m:
            return self.union(n1, n2)
        return self.add(n1, n2)
    def union(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)
        if r1 == r2:
            return False
        self.m[r1] = r2
        return True
    def find(self, n):
        if self.m[n] != n:
            self.m[n] = self.find(self.m[n])
        return self.m[n]

class Solution:
    def findRedundantConnection(self, edges):
        uf = UnionFind()
        for (start, end) in edges:
            if not uf.add_union(start, end):
                return [start, end]

