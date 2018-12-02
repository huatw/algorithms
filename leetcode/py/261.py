'''
1. node has no more than 3 edge
2. no circle
3. all nodes connected
'''
class UnionFind:
    def __init__(self, size):
        self.size = size # check final size == 1
        self.m = {i: i for i in range(size)}

    def union(self, edge): # check circle
        n1, n2 = edge
        r1, r2 = self.find(n1), self.find(n2)
        self.m[r1] = r2
        self.size -= 1
        return r1 != r2

    def find(self, n):
        if self.m[n] != n:
            self.m[n] = self.find(self.m[n])
        return self.m[n]

class Solution:
    def validTree(self, n, edges):
        uf = UnionFind(n)

        return all(map(uf.union, edges)) and uf.size == 1
